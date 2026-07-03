// 閲覧制限：合言葉（共有パスコード）方式。
// パスコードは Pages の暗号化シークレット PASSCODE に保存（リポジトリには置かない）。
// 認証済みの印として SHA-256(PASSCODE+SALT) を HttpOnly クッキーに持たせる。
// 変更するには: echo "新しい合言葉" | npx wrangler pages secret put PASSCODE --project-name kobun-tango
// （変更後は再デプロイで反映。全端末で再ログインが必要になる）

const COOKIE = 'koten_auth';
const SALT = 'koten-v1';
const MAX_AGE = 15552000; // 180日

async function sha256(s) {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(d)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function getCookie(request, name) {
  const h = request.headers.get('Cookie') || '';
  for (const part of h.split(/;\s*/)) {
    const i = part.indexOf('=');
    if (i > 0 && part.slice(0, i) === name) return part.slice(i + 1);
  }
  return '';
}

function loginPage(msg) {
  return new Response(`<!doctype html><html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>古文単語帳｜合言葉</title><style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
  background:#e4e0d3;color:#23201d;font-family:'Zen Kaku Gothic New','Hiragino Sans',sans-serif}
.card{background:#f7f4ec;border:1px solid #d2ccbd;border-radius:16px;padding:30px 26px;width:min(88vw,360px);
  box-shadow:0 8px 22px -16px rgba(38,34,31,.4);text-align:center}
.seal{width:52px;height:52px;border-radius:12px;background:#2f5670;color:#f7f4ec;font-size:28px;
  display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-family:serif}
h1{font-size:19px;margin:0 0 6px}p{font-size:13px;color:#5d564d;margin:0 0 18px;line-height:1.7}
input{width:100%;box-sizing:border-box;font-size:17px;padding:12px;border:1px solid #d2ccbd;border-radius:10px;
  background:#fff;text-align:center;font-family:inherit}
button{width:100%;margin-top:12px;font-size:16px;font-weight:700;padding:13px;border:0;border-radius:10px;
  background:#2f5670;color:#fff;cursor:pointer;font-family:inherit}
.err{color:#8c414c;font-size:13px;font-weight:700;margin:10px 0 0;min-height:1em}
</style></head><body><form class="card" method="POST" action="/login">
<div class="seal">古</div><h1>古文単語帳</h1>
<p>このサイトは生徒専用です。<br>授業で伝えられた合言葉を入力してください。</p>
<input name="passcode" type="password" autocomplete="current-password" placeholder="合言葉" required autofocus>
<button type="submit">入る</button>
<div class="err">${msg || ''}</div>
</form></body></html>`, {
    status: msg ? 401 : 200,
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'X-Robots-Tag': 'noindex' },
  });
}

export async function onRequest(context) {
  const { request, env, next } = context;
  const url = new URL(request.url);

  if (!env.PASSCODE) {
    return new Response('PASSCODE が未設定です。wrangler pages secret put PASSCODE で設定してください。', { status: 503 });
  }
  const token = await sha256(env.PASSCODE + SALT);

  if (url.pathname === '/login') {
    if (request.method === 'POST') {
      let pass = '';
      try { pass = (await request.formData()).get('passcode') || ''; } catch (e) {}
      if (pass.trim() === env.PASSCODE) {
        return new Response(null, {
          status: 302,
          headers: {
            Location: '/',
            'Set-Cookie': `${COOKIE}=${token}; Max-Age=${MAX_AGE}; Path=/; HttpOnly; Secure; SameSite=Lax`,
          },
        });
      }
      return loginPage('合言葉が違います');
    }
    if (getCookie(request, COOKIE) === token) {
      return Response.redirect(new URL('/', url).toString(), 302);
    }
    return loginPage('');
  }

  if (getCookie(request, COOKIE) !== token) {
    // ページ遷移はログイン画面へ。SW等のサブリソース要求は401（キャッシュ汚染を防ぐ）
    if (request.headers.get('Sec-Fetch-Mode') === 'navigate' || request.mode === 'navigate') {
      return Response.redirect(new URL('/login', url).toString(), 302);
    }
    return new Response('unauthorized', { status: 401 });
  }

  const res = await next();
  const out = new Response(res.body, res);
  out.headers.set('X-Robots-Tag', 'noindex'); // 検索エンジンに載せない
  return out;
}
