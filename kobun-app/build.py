# -*- coding: utf-8 -*-
import pandas as pd, re, json, os
ROOT=os.path.dirname(os.path.abspath(__file__))

SRC = os.path.join(ROOT,'data','kobun-words.xlsx')
df = pd.read_excel(SRC, sheet_name='リストa', header=1)
df.columns = ['idxA','idxB','no','word','pos','keigo','imi','ko','koBlank','yk','ykBlank',
              'no2','word2','imi2','ko2','koBlank2','yk2','ykBlank2']
df = df.dropna(subset=['no']).copy(); df['no']=df['no'].astype(int)

cl_imi  = lambda s: re.sub(r'[〔〕\s　]','',str(s)).strip() if pd.notna(s) else ''
cl_txt  = lambda s: str(s).strip() if pd.notna(s) else ''
def cl_yk(s):
    s=cl_txt(s); return re.sub(r'^[　\s]*[（(]訳[）)]','',s).strip()
def src_of(ko):
    m=re.findall(r'（([^（）]+)）',cl_txt(ko)); return m[-1] if m else ''
def strip_src(ko):
    return re.sub(r'\s*（[^（）]+）\s*$','',cl_txt(ko)).strip()

BL_RE=re.compile(r'〔[\s　]*[〕\]）]')
def ko_underline(ko, koBlank):
    s=strip_src(ko); kb=strip_src(koBlank)
    if '〔' not in kb: return s
    lits=BL_RE.split(kb)
    if len(lits)<2: return s
    rest=s; out=''; ok=True
    for i in range(len(lits)-1):
        lit=lits[i]; nxt=lits[i+1]
        if lit:
            p=rest.find(lit)
            if p<0: ok=False; break
            out+=rest[:p+len(lit)]; rest=rest[p+len(lit):]
        q=rest.find(nxt) if nxt else len(rest)
        if q<0: ok=False; break
        out+='\x01'+rest[:q]+'\x02'; rest=rest[q:]
    out+=rest
    return out if ok else s

# ---------- meaning consolidation (merge example-answers of the same sense) ----------
try:
    import fugashi
    _TAGGER=fugashi.Tagger()
    def lemmatize(label):
        try:
            ws=_TAGGER(label)
            if not ws: return label
            last=ws[-1]
            base=getattr(last.feature,'orthBase',None) or getattr(last.feature,'lemma',None) or last.surface
            return label[:len(label)-len(last.surface)]+base
        except Exception:
            return label
except Exception:
    def lemmatize(label): return label
ALLOWED={'', 'る','れ','れる','られ','られる','り','ら','ろ','っ','た','て','だ','で',
 'い','く','き','かっ','かろ','けれ','しい','しく','しき','しかっ','じ',
 'こと','ること','の','ものだ',
 'な','に','なり','なる','なら','なっ','なれ','だっ','であ','である',
 'ず','ぬ','ね','ない','なく','なかっ',
 'する','すれ','しろ','せよ','した','して',
 'う','よ','よう','ます','まし','ませ','ましょ','さ','せ','し','す','む','み','ま','め','ば','べ','わ','を','ん','も','や'}
TERM=('る','い','な','り','だ','なり','う','む','ぐ','ぶ','つ','ぬ','す','ない','する')
OVERRIDE={'亡くなっ':'亡くなる','いらっしゃっ':'いらっしゃる','召し上がら':'召し上がる',
 'お召しになっ':'お召しになる','不平を言った':'不平を言う','管絃を楽しみ':'管絃を楽しむ',
 'お召しになれ':'お召しになる','妨げられず':'妨げられる','華やかに':'華やかだ','突然の':'突然だ'}
def _collapse(s):
    n=len(s)
    return s[:n//2] if (n>=2 and n%2==0 and s[:n//2]==s[n//2:]) else s
def _cp(a,b):
    i=0
    while i<len(a) and i<len(b) and a[i]==b[i]: i+=1
    return i
def _same(a,b):
    a=_collapse(a); b=_collapse(b)
    if a==b: return True
    c=_cp(a,b)
    if c<1: return False
    return a[c:] in ALLOWED and b[c:] in ALLOWED
def cluster_meanings(ms):
    cs=[]
    for m in ms:
        for c in cs:
            if any(_same(m,x) for x in c): c.append(m); break
        else: cs.append([m])
    return cs
def canon_label(c):
    def sc(s):
        s2=_collapse(s); return (1 if s2.endswith(TERM) else 0, len(s2))
    lab=_collapse(max(c,key=sc))
    return OVERRIDE.get(lab,lab)

def importance(no):
    if no<=50:return '最必修'
    if no<=150:return '必修'
    if no<=180:return '必修敬語'
    if no<=280:return '重要'
    return '応用'

KEIGO={151:['尊敬'],152:['尊敬'],153:['尊敬'],154:['尊敬'],155:['謙譲'],156:['謙譲'],
 157:['尊敬'],158:['尊敬'],159:['尊敬'],160:['丁寧'],161:['尊敬'],162:['謙譲'],163:['謙譲'],
 164:['謙譲','尊敬'],165:['丁寧','謙譲'],166:['丁寧','謙譲'],167:['尊敬'],168:['謙譲'],
 169:['謙譲','尊敬'],170:['謙譲'],171:['謙譲'],172:['謙譲'],173:['尊敬'],174:['尊敬'],
 175:['謙譲'],176:['尊敬'],177:['尊敬'],178:['尊敬'],179:['謙譲'],180:['謙譲']}

TL={'LOVE':'恋・男女','DEATH':'病・死・別れ','BUD':'仏道・信仰','COURT':'宮廷・身分',
 'BEAUTY':'美・優雅・情趣','GOOD':'よい評価','BAD':'わるい評価','PAIN':'心情・つらさ',
 'AFF':'心情・いとしさ','ANX':'不安・気がかり','THINK':'思考・うわさ','TIME':'時・季節・自然','WORD':'ことば・学問'}
THEME_ORDER=['LOVE','DEATH','BUD','COURT','BEAUTY','GOOD','BAD','PAIN','AFF','ANX','THINK','TIME','WORD']
TH={1:['THINK'],2:['THINK'],3:['BUD'],4:['THINK'],5:['LOVE'],6:['PAIN'],7:['LOVE','THINK'],8:['LOVE'],
 12:['AFF'],13:['AFF'],14:['GOOD','BAD'],15:['BEAUTY'],16:['GOOD','COURT'],17:['BAD','COURT'],
 19:['THINK'],20:['ANX'],21:['GOOD'],22:['GOOD'],23:['PAIN'],24:['PAIN'],25:['PAIN'],26:['BEAUTY'],
 29:['PAIN'],31:['TIME'],34:['BUD'],35:['WORD'],36:['WORD'],38:['BEAUTY','LOVE'],39:['LOVE'],
 45:['TIME'],51:['BEAUTY'],54:['BEAUTY'],60:['THINK'],66:['DEATH','BUD'],69:['DEATH'],70:['PAIN'],
 72:['DEATH'],73:['BUD'],74:['GOOD','BEAUTY'],75:['GOOD'],76:['COURT'],77:['GOOD','BAD'],78:['GOOD'],
 79:['BEAUTY'],82:['BEAUTY'],84:['PAIN'],85:['ANX'],86:['PAIN','AFF'],87:['BAD'],88:['GOOD'],89:['LOVE'],
 90:['BAD'],91:['BAD'],92:['BAD'],93:['BAD'],94:['BAD'],95:['BAD'],96:['BAD'],97:['PAIN'],98:['BAD'],
 99:['COURT','BEAUTY'],100:['BEAUTY'],103:['TIME'],104:['BAD'],105:['LOVE'],107:['BAD'],108:['COURT'],
 109:['COURT'],110:['BUD'],113:['BUD'],114:['THINK','LOVE'],115:['DEATH'],117:['TIME'],118:['TIME'],
 121:['LOVE'],125:['WORD'],127:['TIME'],128:['TIME'],129:['TIME'],145:['TIME'],147:['THINK'],
 181:['COURT'],184:['WORD'],188:['LOVE'],189:['LOVE'],195:['LOVE','COURT'],197:['DEATH'],198:['PAIN'],
 199:['PAIN'],200:['PAIN'],201:['DEATH'],202:['DEATH'],203:['DEATH'],204:['DEATH'],205:['DEATH'],
 209:['BAD'],210:['BEAUTY'],212:['LOVE','BEAUTY'],213:['BEAUTY'],214:['BEAUTY'],218:['GOOD'],
 220:['ANX'],221:['PAIN','ANX'],223:['GOOD'],224:['BAD'],229:['BAD'],230:['PAIN'],231:['TIME'],
 233:['PAIN'],234:['PAIN'],237:['BAD'],238:['BAD'],240:['DEATH'],242:['BAD'],250:['TIME'],251:['LOVE'],
 252:['BEAUTY'],253:['AFF'],254:['BEAUTY'],255:['COURT'],256:['COURT'],257:['COURT'],261:['WORD'],
 263:['WORD'],264:['WORD'],265:['COURT'],267:['LOVE'],273:['TIME'],275:['TIME'],281:['THINK'],
 285:['PAIN'],287:['COURT'],288:['BEAUTY'],291:['ANX'],294:['PAIN'],298:['LOVE','BEAUTY'],299:['BEAUTY'],
 304:['WORD'],309:['TIME'],310:['COURT'],311:['TIME'],312:['TIME'],323:['BAD'],326:['LOVE'],329:['TIME']}

# learning-flag sets
GAP_BIG={2,15,17,19,21,26,38,66,73,77,82,84,86,93,98,99,105,114,140,147,195,207,208,237}
GAP_SMALL={1,5,7,8,9,11,12,13,16,18,25,28,55,60,69,74,78,79,87,89,210,212,213,217,222,223,230,298,326}
CORE={1,4,5,7,10,14,15,20,26,37,38,40,60,64,67,77,78,85,120,233}
POLAR={14,77,87,140}
KANGO={3,65,179,180,191,193,197}
KEIGO_CARE={153,164,167,169}

# ---------- assemble base ----------
WORD={}; base=[]
for no,sub in df.groupby('no'):
    word=cl_txt(sub['word'].iloc[0]); WORD[no]=word
    pos=cl_txt(sub['pos'].iloc[0]); is_k=sub['keigo'].notna().any()
    meanings=[]; ex=[]
    for _,r in sub.iterrows():
        imi=cl_imi(r['imi'])
        if imi and imi not in meanings: meanings.append(imi)
        ex.append({'imi':imi,'ko':strip_src(r['ko']),'koBlank':strip_src(r['koBlank']),
                   'koU':ko_underline(r['ko'],r['koBlank']),
                   'yk':cl_yk(r['yk']),'ykBlank':cl_yk(r['ykBlank']),'src':src_of(r['ko'])})
    clusters=cluster_meanings(meanings)
    raw_labels=[canon_label(c) for c in clusters]
    llabels=[lemmatize(l) for l in raw_labels]
    final=[]; cl2final=[]
    for l in llabels:
        if l in final: cl2final.append(final.index(l))
        else: final.append(l); cl2final.append(len(final)-1)
    imi2fi={}
    for i,c in enumerate(clusters):
        for m in c: imi2fi[m]=cl2final[i]+1
    for e in ex: e['mi']=imi2fi.get(e['imi'],0)
    base.append({'no':no,'word':word,'pos':pos,'imp':importance(no),
                 'keigo':KEIGO.get(no,[]),'meanings':final,'examples':ex})

# ---------- relations (類義/対義/混同), per-sense ----------
def S(*pairs): return list(pairs)
SYN=[
 S((3,'がまんする'),(5,'がまんする')),
 S((24,'つらい'),(25,'つらい'),(221,'つらい・気の毒'),(233,'つらい')),
 S((12,'かわいい'),(13,'いとしい'),(86,'いとしい・気の毒'),(253,'かわいらしい')),
 S((20,'気がかり'),(85,'待ち遠しい・不安'),(220,'心配'),(291,'気が晴れない')),
 S((14,'すばらしい'),(21,'立派'),(22,'すばらしい'),(88,'すばらしい'),(74,'すばらしい')),
 S((15,'趣がある'),(26,'しみじみ'),(74,'興趣がある')),
 S((7,'結婚する'),(8,'結婚する'),(189,'男のもとに通う')),
 S((66,'訪れる・見舞う'),(186,'訪ねる・手紙を出す')),
 S((69,'患う・思い悩む'),(204,'病気で苦しむ'),(197,'疲れる'),(201,'病気になる')),
 S((72,'亡くなる'),(205,'先立たれる')),
 S((99,'高貴だ'),(76,'高貴だ'),(16,'身分が高い')),
 S((213,'優美だ'),(254,'優美だ'),(288,'気品がある'),(210,'奥ゆかしい'),(100,'美しい')),
 S((29,'退屈・もの寂しい'),(97,'物足りない')),
 S((2,'評判になる'),(147,'うわさに聞く'),(114,'評判'),(60,'世間に知られる')),
 S((127,'すぐに'),(128,'早く'),(129,'早く'),(45,'すぐに')),
 S((62,'準備する'),(206,'用意する'),(305,'準備')),
 S((42,'たくさん'),(269,'たくさん')),
 S((251,'ひそかに'),(274,'そっと')),
 S((4,'思われる'),(7,'思われる')),
]
CONF=[
 S((1,'目を覚ます'),(87,'驚きあきれる'),(237,'気にくわない')),
 S((22,'すばらしい'),(55,'愛する・感嘆'),(218,'感じよい'),(237,'気にくわない')),
 S((155,'申し上げる(謙)'),(168,'参上する(謙)'),(171,'退出する(謙)'),(172,'退出する(謙)'),(169,'参上/差し上げる'),(170,'差し上げる(謙)')),
 S((159,'お与えになる(尊・四段)'),(160,'〜ております(丁・下二)')),
 S((16,'よし＝形容詞'),(122,'よし＝名詞')),
 S((110,'しるし＝名詞(効果)'),(292,'しるし＝形容詞(明白)')),
 S((60,'聞こゆ＝動詞(聞こえる)'),(156,'きこゆ＝敬語(申し上げる)')),
 S((45,'そのまま'),(137,'そのまま・全部'),(316,'そのまま')),
 S((19,'ゆかし＝〜したい'),(77,'ゆゆし＝不吉/立派')),
 S((21,'ありがたし＝めったにない'),(208,'かたじけなし＝おそれ多い')),
 S((89,'つれなし＝冷淡'),(29,'つれづれ＝退屈')),
 S((90,'あいなし＝つまらない'),(91,'あぢきなし＝どうにもならない'),(95,'よしなし＝つまらない')),
 S((69,'患う'),(204,'病気'),(202,'静養する'),(203,'病が癒える'),(240,'病が重い')),
]
ANT=[((99,'高貴だ'),(17,'身分が低い')),((76,'高貴だ'),(17,'身分が低い')),
 ((16,'身分が高い'),(17,'身分が低い・粗末')),((21,'めったにない'),(325,'ありきたりだ')),
 ((21,'めったにない'),(130,'総じて・普通')),((117,'早朝'),(275,'一晩中'))]

rel={no:[] for no in WORD}
def add_clusters(cls,typ):
    for cl in cls:
        for a,sa in cl:
            for b,sb in cl:
                if a==b or b not in WORD:continue
                rel[a].append({'type':typ,'sense':sa,'no':b,'word':WORD[b],'gloss':sb})
def add_ant(pairs):
    for (a,sa),(b,sb) in pairs:
        if a in WORD and b in WORD:
            rel[a].append({'type':'対義','sense':sa,'no':b,'word':WORD[b],'gloss':sb})
            rel[b].append({'type':'対義','sense':sb,'no':a,'word':WORD[a],'gloss':sa})
add_clusters(SYN,'類義'); add_clusters(CONF,'混同'); add_ant(ANT)
# dedup by (type,no) keeping first
for no in rel:
    seen=set(); out=[]
    for r in rel[no]:
        k=(r['type'],r['no'])
        if k in seen:continue
        seen.add(k); out.append(r)
    rel[no]=out

# ---------- finalize words ----------
FL={'GAPB':'現代語とギャップ大','GAPS':'現代語と少しズレ','POLY':'多義語','CORE':'コアで覚える',
    'POLAR':'プラス/マイナス両義','KOOU':'呼応の副詞','NASHI':'「〜なし」型','KANGO':'漢語サ変','KEIGOCARE':'敬語要注意'}
FLAG_ORDER=['GAPB','GAPS','POLY','CORE','POLAR','KOOU','NASHI','KANGO','KEIGOCARE']
words=[]
for w in base:
    no=w['no']; flags=[]
    if no in GAP_BIG: flags.append(FL['GAPB'])
    elif no in GAP_SMALL: flags.append(FL['GAPS'])
    if len(w['meanings'])>=4: flags.append(FL['POLY'])
    if no in CORE: flags.append(FL['CORE'])
    if no in POLAR: flags.append(FL['POLAR'])
    if '～' in w['word']: flags.append(FL['KOOU'])
    if w['pos']=='形容詞' and w['word'].endswith('なし'): flags.append(FL['NASHI'])
    if no in KANGO: flags.append(FL['KANGO'])
    if no in KEIGO_CARE: flags.append(FL['KEIGOCARE'])
    w['themes']=[TL[c] for c in TH.get(no,[])]
    w['flags']=flags
    w['related']=rel[no]
    words.append(w)
words.sort(key=lambda x:x['no'])

# ---------- attach explanations from MD ----------
import os
NOTE_MD=os.path.join(ROOT,'data','explanations.md')
notes={}; kanji={}
if os.path.exists(NOTE_MD):
    npat=re.compile(r'^(\d{1,3})\s+(.+?)\s+[—–-]\s+(.+)$')
    for ln in open(NOTE_MD,encoding='utf-8').read().split('\n'):
        m=npat.match(ln.strip())
        if m:
            no=int(m.group(1)); head=m.group(2).strip(); body=m.group(3).strip()
            notes[no]=body
            km=re.search(r'[（(](.+?)[）)]',head)
            if km: kanji[no]=km.group(1).strip()
for w in words:
    w['note']=notes.get(w['no'],'')
    w['kanji']=kanji.get(w['no'],'')
print('解説付与:',sum(1 for w in words if w['note']),'/',len(words),'| 漢字付与:',sum(1 for w in words if w['kanji']))

meta={'imp':['最必修','必修','必修敬語','重要','応用'],
 'pos':['動詞','形容詞','形容動詞','名詞','副詞','連体詞・連語'],
 'keigo':['尊敬','謙譲','丁寧'],
 'theme':[TL[c] for c in THEME_ORDER],
 'flag':[FL[c] for c in FLAG_ORDER],'total':len(words)}

json.dump({'words':words,'meta':meta},open(os.path.join(ROOT,'build','data_payload.json'),'w',encoding='utf-8'),ensure_ascii=False)
print('words',len(words),'| theme',sum(1 for w in words if w['themes']),
      '| flag',sum(1 for w in words if w['flags']),
      '| related',sum(1 for w in words if w['related']))
from collections import Counter
fc=Counter(f for w in words for f in w['flags'])
for k in meta['flag']:print(' ',k,fc.get(k,0))
