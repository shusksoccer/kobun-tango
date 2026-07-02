# -*- coding: utf-8 -*-
import os
ROOT=os.path.dirname(os.path.abspath(__file__))
DATA = open(os.path.join(ROOT,'build','data_payload.json'), encoding='utf-8').read()

CSS = r"""
*{box-sizing:border-box}
:root{
  --paper:#e4e0d3; --card:#f7f4ec; --ink:#23201d; --ink2:#5d564d; --ink3:#8a8276; --rule:#d2ccbd;
  --hanada:#2f5670; --hanada-d:#21425a; --suo:#8c414c; --seiji:#5f8472; --kikyo:#5f5480; --kincha:#8a6d3f;
  --shadow:0 1px 2px rgba(38,34,31,.05), 0 8px 22px -16px rgba(38,34,31,.4);
  --tap:44px;
}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:'Zen Kaku Gothic New','Hiragino Sans','Yu Gothic UI','Noto Sans JP',sans-serif;
  line-height:1.7;font-feature-settings:"palt";-webkit-font-smoothing:antialiased}
.mincho{font-family:'Shippori Mincho B1','Shippori Mincho','Hiragino Mincho ProN','Yu Mincho','Noto Serif JP',serif}
a{color:var(--hanada-d)}
.wrap{max-width:860px;margin:0 auto;padding:0 14px}
button{font-family:inherit}

/* top bar */
.topbar{position:sticky;top:0;z-index:40;background:rgba(228,224,211,.94);
  backdrop-filter:saturate(1.1) blur(8px);border-bottom:1px solid var(--rule)}
.topbar .row{display:flex;align-items:center;gap:10px;padding:10px 0}
.brand{font-weight:700;font-size:18px;letter-spacing:.03em;display:flex;align-items:baseline;gap:6px;min-width:0}
.brand .seal{font-family:'Shippori Mincho B1',serif;color:var(--card);background:var(--suo);
  border-radius:4px;padding:3px 8px;font-size:16px;letter-spacing:.1em}
.brand small{color:var(--ink2);font-weight:500;font-size:11px;letter-spacing:.01em;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.topnav{margin-left:auto;flex:none}
.btnlink{display:inline-block;text-decoration:none;border:1px solid var(--hanada);color:var(--hanada-d);
  border-radius:999px;padding:9px 16px;font-size:14px;font-weight:700;background:#fff8;line-height:1}
.btnlink.solid{background:var(--hanada);color:#fff;border-color:var(--hanada)}
.btnlink:active{transform:scale(.97)}

/* controls */
.controls{padding:12px 0 4px;display:grid;gap:9px}
.search{display:flex;align-items:center;background:var(--card);border:1px solid var(--rule);
  border-radius:12px;padding:0 12px;min-height:var(--tap)}
.search input{flex:1;border:0;background:transparent;padding:11px 8px;font-size:16px;color:var(--ink);font-family:inherit;outline:none;min-width:0}
.search svg{flex:none;opacity:.5}
.ctlrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
select,.minibtn{font-family:inherit;font-size:14px;color:var(--ink);background:var(--card);border:1px solid var(--rule);
  border-radius:10px;padding:0 12px;min-height:var(--tap);cursor:pointer}
.minibtn{font-weight:600}
.minibtn.act{background:var(--hanada);color:#fff;border-color:var(--hanada)}
.count{color:var(--ink2);font-size:12.5px;margin-left:auto;white-space:nowrap;text-align:right}
.count b{color:var(--seiji)}

/* filters */
.filters{margin:6px 0 2px;border:1px solid var(--rule);border-radius:14px;background:#fbf9f3;overflow:hidden}
.filters[hidden]{display:none}
.filterbar{display:flex;align-items:center;gap:10px;padding:11px 14px;background:#efece2;font-size:12.5px;color:var(--ink2)}
.filterbar .clear{margin-left:auto;color:var(--suo);background:none;border:0;cursor:pointer;font-family:inherit;font-size:13px;min-height:36px}
.facet{padding:10px 14px;border-top:1px solid var(--rule)}
.facet h4{margin:0 0 8px;font-size:11.5px;letter-spacing:.12em;color:var(--ink2);font-weight:700}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-family:inherit;font-size:13.5px;border-radius:999px;padding:8px 14px;cursor:pointer;
  border:1px solid var(--c,var(--rule));color:var(--c,var(--ink2));background:transparent;line-height:1.2}
.chip:active{transform:scale(.97)}
.chip.on{background:var(--c,var(--ink));color:#fff;border-color:var(--c,var(--ink))}

/* list + card */
.list{padding:12px 0 96px;display:grid;gap:12px}
.card{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--impc,var(--rule));
  border-radius:14px;padding:13px 15px 12px;box-shadow:var(--shadow);scroll-margin-top:120px}
.card.flash{animation:flash 1.6s ease}
@keyframes flash{0%{box-shadow:0 0 0 3px var(--hanada)}100%{box-shadow:var(--shadow)}}
.card.learned{opacity:.5}
.card.learned .word{text-decoration:line-through;text-decoration-color:var(--ink3)}
.ctop{display:flex;align-items:flex-start;gap:10px}
.known{flex:none;width:34px;height:34px;border-radius:50%;border:1.5px solid var(--rule);background:#fff6;
  color:var(--seiji);font-weight:900;font-size:15px;cursor:pointer;margin-top:3px;display:flex;align-items:center;justify-content:center;
  position:relative}
.known::before{content:'';position:absolute;inset:-5px}/* タップ領域を44pxに拡大 */
.known[aria-pressed="true"]{background:var(--seiji);border-color:var(--seiji);color:#fff}
.known.partial{background:#e7e2d4;border-color:var(--seiji);color:var(--seiji)}
.hwblock{flex:1;min-width:0}
.hwline{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.no{font-family:'Shippori Mincho B1',serif;color:var(--ink3);font-size:12px;border:1px solid var(--rule);border-radius:5px;padding:1px 6px}
.word{font-size:clamp(26px,7.4vw,31px);font-weight:600;letter-spacing:.01em;line-height:1.18}
.kanji{font-size:13px;color:var(--ink3);font-family:'Shippori Mincho B1',serif;margin-left:1px;white-space:nowrap}
.body2{display:flex;flex-direction:column;gap:11px;margin-top:2px}
.body2 .means,.body2 .mlist{margin-top:9px}
.noteprev{display:block;text-align:left;background:#f4eff5;border:1px solid #e2d8e4;border-radius:12px;
  padding:11px 13px;cursor:pointer;color:var(--ink);font-family:inherit;width:100%}
.noteprev:active{transform:scale(.995)}
.noteprev .lbl{display:flex;justify-content:space-between;align-items:center;gap:8px;font-size:11px;font-weight:700;letter-spacing:.08em;color:#5f5480}
.noteprev .lbl .more{font-weight:700;white-space:nowrap}
.noteprev .snip{font-size:13.5px;line-height:1.8;margin-top:6px;color:var(--ink2);
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
@media(min-width:680px){
  .body2{flex-direction:row;align-items:flex-start;gap:14px}
  .body2 .means,.body2 .means.one,.body2 .mlist{flex:1;margin-top:0}
  .noteprev{flex:0 0 46%;max-width:330px}
  .noteprev .snip{-webkit-line-clamp:6}
}
.modal{position:fixed;inset:0;z-index:100;display:flex;align-items:flex-end;justify-content:center;background:rgba(35,32,29,.5)}
.modal[hidden]{display:none}
.modal-card{background:var(--card);width:100%;max-width:560px;border-radius:18px 18px 0 0;padding:18px 18px 28px;
  max-height:84vh;overflow-y:auto;-webkit-overflow-scrolling:touch;box-shadow:0 -8px 30px rgba(0,0,0,.28);animation:sheet .22s ease}
@keyframes sheet{from{transform:translateY(24px);opacity:.5}to{transform:none;opacity:1}}
.modal-x{position:sticky;top:0;float:right;width:38px;height:38px;border-radius:50%;border:1px solid var(--rule);
  background:#fff;font-size:21px;line-height:1;cursor:pointer;color:var(--ink2)}
.modal-eyebrow{font-size:11px;letter-spacing:.12em;color:var(--kikyo);font-weight:700;margin-bottom:4px}
.modal-title{font-size:27px;font-weight:600;line-height:1.2}
.modal-title .ktitle{font-size:16px;color:var(--ink2);margin-left:8px;font-family:'Shippori Mincho B1',serif}
.modal-sub{margin:9px 0 13px;font-size:14px;color:var(--ink2);display:flex;flex-wrap:wrap;gap:7px;align-items:center;line-height:1.5}
.modal-sub .badge{color:#fff}
.modal-body{font-size:16px;line-height:2;color:var(--ink)}
@media(min-width:760px){.modal{align-items:center;padding:20px}.modal-card{border-radius:18px}}
.imp{font-size:11.5px;font-weight:700;letter-spacing:.04em;margin-left:auto}
.metaline{display:flex;flex-wrap:wrap;gap:6px;margin-top:7px;align-items:center}
.pos{font-size:11.5px;font-weight:700;color:#fff;background:#7a7264;border-radius:6px;padding:3px 8px}
.kat{font-size:11.5px;font-weight:700;color:#6c655a;border:1px solid #b8b0a0;border-radius:6px;padding:2px 7px}
.kg{font-size:11.5px;font-weight:700;color:#fff;background:var(--c,#666);border-radius:6px;padding:3px 8px}
.tag{font-size:12px;border-radius:999px;padding:6px 12px;cursor:pointer;border:1px solid var(--c,var(--rule));
  color:var(--c,var(--ink2));background:transparent;line-height:1.3}
.tag.flag{border-style:dashed;font-weight:700}
.tag:active{transform:scale(.97)}
.means{margin:11px 0 2px;padding:0;list-style:none;counter-reset:m;display:grid;gap:5px}
.means li{position:relative;padding-left:1.7em;font-size:17.5px;line-height:1.55;color:var(--ink)}
.means li::before{counter-increment:m;content:counter(m);position:absolute;left:0;top:.12em;
  width:1.25em;height:1.25em;border-radius:50%;background:#e7e2d4;color:var(--hanada-d);
  font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center}
.means.one{padding-left:0;font-size:18px;line-height:1.5;color:var(--ink)}
/* per-sense checkable meaning list */
.mlist{margin:11px 0 2px;padding:0;list-style:none;display:grid;gap:8px}
.mrow{display:flex;align-items:flex-start;gap:9px;font-size:17.5px;line-height:1.5;color:var(--ink)}
.mchk{flex:none;width:28px;height:28px;border-radius:50%;border:1.5px solid var(--rule);
  background:#e7e2d4;color:var(--hanada-d);font-size:11px;font-weight:700;cursor:pointer;line-height:1;
  display:flex;align-items:center;justify-content:center;padding:0;position:relative}
.mchk::before{content:'';position:absolute;inset:-6px}/* タップ領域を40pxに拡大 */
.mrow.on .mchk{background:var(--seiji);border-color:var(--seiji);color:#fff}
.mtext{flex:1;min-width:0}
.mrow.on .mtext{color:var(--ink3);text-decoration:line-through;text-decoration-color:var(--ink3)}
.mrow.tested .mtext{font-weight:700}
.testedtag{display:inline-block;font-size:10.5px;font-weight:700;color:var(--hanada-d);background:#f0e4c8;
  border-radius:6px;padding:1px 7px;margin-left:7px;white-space:nowrap;vertical-align:middle}
.themerow{display:flex;flex-wrap:wrap;gap:7px;margin-top:10px}
.tag.th{opacity:.95}
.discl{display:flex;flex-wrap:wrap;gap:8px;margin-top:11px}
.disc{font-family:inherit;font-size:13px;font-weight:600;color:var(--hanada-d);background:#eef1f0;
  border:1px solid #d8e0dd;border-radius:9px;padding:8px 13px;cursor:pointer;min-height:38px}
.disc.open{background:var(--hanada);color:#fff;border-color:var(--hanada)}
.panel{display:none;margin-top:10px;border-top:1px dashed var(--rule);padding-top:10px}
.panel.open{display:block}
/* examples */
.ex{padding:9px 0;border-top:1px solid #ece8dd}.ex:first-child{border-top:0}
.ex .exno{font-size:12px;color:var(--suo);font-weight:700;letter-spacing:.04em;margin-bottom:3px}
.ex .ko{font-size:16.5px;margin:2px 0 7px;line-height:1.95}
.ex .yk{font-size:14px;color:var(--ink2);background:#efece2;border-radius:8px;padding:8px 11px;line-height:1.7}
.ex .src{font-size:11.5px;color:var(--ink3);margin-top:5px}
.blank{color:var(--suo);font-weight:700}
.exred{color:var(--suo);font-weight:700}
.exmask{color:transparent;background:var(--suo);border-radius:3px;cursor:pointer;padding:0 2px;transition:.15s;user-select:none;-webkit-user-select:none}
.exmask.open{color:var(--ink);background:rgba(140,65,76,.15)}
/* related */
.rellabel{font-size:11px;letter-spacing:.1em;color:var(--ink2);font-weight:700;margin-bottom:7px}
.relgroup{margin:7px 0;display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.relsense{font-size:12.5px;color:var(--ink);background:#e7e2d4;border-radius:6px;padding:3px 9px;font-weight:700}
.reltype{font-size:10.5px;font-weight:700;border-radius:5px;padding:2px 7px;color:#fff}
.rt-類義{background:#5f8472}.rt-対義{background:#8c414c}.rt-混同{background:#8a6d3f}
.relw{font-family:inherit;font-size:13.5px;background:#fff8;border:1px solid var(--rule);border-radius:999px;
  padding:6px 12px;cursor:pointer;color:var(--hanada-d);min-height:36px}
.relw small{color:var(--ink3);margin-left:5px;font-size:11px}
.relw:active{transform:scale(.97)}
.empty{text-align:center;color:var(--ink2);padding:60px 20px}

/* quiz */
.qsetup,.qplay,.qdone{padding:16px 0 100px}
.qsetup h2{font-size:18px;margin:14px 0 4px;letter-spacing:.03em}
.qsetup p.help{color:var(--ink2);font-size:13px;margin:0 0 14px}
.field{background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:13px 15px;margin-bottom:11px}
.field h4{margin:0 0 9px;font-size:12.5px;letter-spacing:.06em;color:var(--ink2)}
.row{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.modebtns{display:grid;gap:9px}
.modebtn{text-align:left;font-family:inherit;background:#fff8;border:1px solid var(--rule);border-radius:12px;padding:13px 15px;cursor:pointer}
.modebtn.on{border-color:var(--hanada);background:#eaf0f4;box-shadow:inset 0 0 0 1px var(--hanada)}
.modebtn b{font-size:15px}.modebtn span{display:block;color:var(--ink2);font-size:12px;margin-top:3px}
.reviewbox{border:1px dashed var(--seiji);border-radius:12px;background:#eef3ee;padding:11px 13px}
.reviewinfo{font-size:13.5px;color:var(--ink2);font-weight:600}
/* 四択 */
.mcgrid{display:grid;gap:9px;margin-top:14px;text-align:left;max-width:560px;margin-left:auto;margin-right:auto}
.mcbtn{font-family:inherit;font-size:15.5px;line-height:1.5;text-align:left;padding:12px 14px;min-height:48px;
  border:1px solid var(--rule);border-radius:12px;background:#fff8;cursor:pointer;color:var(--ink);
  display:flex;align-items:center;gap:10px}
.mcbtn .mck{flex:none;width:24px;height:24px;border-radius:50%;background:#e7e2d4;color:var(--hanada-d);
  font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center}
.mcbtn.ok{border-color:var(--seiji);background:#e6efe6;box-shadow:inset 0 0 0 1px var(--seiji)}
.mcbtn.ok .mck{background:var(--seiji);color:#fff}
.mcbtn.ng{border-color:#8c414c;background:#f4e7e7}
.mcbtn.ng .mck{background:#8c414c;color:#fff}
.mcbtn:disabled{cursor:default;opacity:.92}
/* 学習レポート */
.rep{display:flex;align-items:center;gap:8px;margin:5px 0}
.replabel{flex:0 0 10.5em;font-size:12.5px;color:var(--ink2)}
.repbar{flex:1;height:10px;background:#e7e2d4;border-radius:99px;overflow:hidden}
.repbar i{display:block;height:100%;border-radius:99px}
.repnum{flex:0 0 3.8em;text-align:right;font-size:12px;color:var(--ink2);font-variant-numeric:tabular-nums}
.repline{font-size:15.5px;margin-bottom:4px}
#repBody h4{margin:16px 0 7px;font-size:12.5px;letter-spacing:.08em;color:var(--kikyo)}
.repweak{display:flex;flex-wrap:wrap;gap:7px}
.bignum{font-family:'Shippori Mincho B1',serif;font-size:30px;color:var(--hanada-d);line-height:1}
.start{font-family:inherit;font-size:17px;font-weight:700;background:var(--hanada);color:#fff;border:0;border-radius:12px;
  padding:15px 30px;cursor:pointer;box-shadow:var(--shadow);width:100%;max-width:360px}
.start:disabled{opacity:.4}
.progress{height:7px;background:#d9d3c4;border-radius:99px;overflow:hidden;margin:4px 0 14px}
.progress i{display:block;height:100%;background:var(--seiji);transition:width .3s}
.qmeta{display:flex;align-items:center;gap:10px;color:var(--ink2);font-size:13px;margin-bottom:8px}
.qcard{background:var(--card);border:1px solid var(--rule);border-radius:18px;padding:22px 16px;box-shadow:var(--shadow);text-align:center}
.qbadge{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:8px}
.qbadge .pos,.qbadge .kg,.qbadge .imp2{font-size:11px;color:#fff;border-radius:6px;padding:3px 8px;font-weight:700}
.qword{font-size:clamp(30px,9vw,40px);font-weight:600;margin:8px 0 14px;line-height:1.2}
.qword.rev{font-size:clamp(20px,5.6vw,25px);line-height:1.5}
.qkolabel{font-size:11px;letter-spacing:.1em;color:var(--ink3);margin-bottom:4px}
.qko{font-size:17px;line-height:1.95;color:var(--ink);background:#efece2;border-radius:12px;padding:14px 14px;margin:0 auto;max-width:620px;text-align:left}
.qhintlabel{font-size:11px;letter-spacing:.08em;color:var(--ink3);margin:9px auto 3px;max-width:620px;text-align:left}
.hintbtn{font-family:inherit;font-size:13px;font-weight:700;color:var(--hanada-d);background:#eef1f0;
  border:1px solid #d8e0dd;border-radius:9px;padding:9px 15px;cursor:pointer;margin:11px auto 0;display:block;min-height:40px}
.hintbtn[hidden]{display:none}
.qhint{font-size:14px;line-height:1.8;color:var(--ink2);background:#f0ede4;border:1px solid #e3ddcf;border-radius:10px;padding:10px 13px;margin:0 auto;max-width:620px;text-align:left}
.qsrc{font-size:11.5px;color:var(--ink3);margin-top:6px}
.qprompt{color:var(--ink2);font-size:13.5px;margin:15px 0}
.reveal{display:none;text-align:left;max-width:620px;margin:14px auto 0;border-top:1px dashed var(--rule);padding-top:14px}
.reveal.show{display:block}
.reveal .ans{font-size:25px;font-weight:700;color:var(--hanada-d);margin-bottom:8px}
.reveal .full{font-size:16px;line-height:1.9;margin:6px 0}
.reveal .tr{font-size:13.5px;color:var(--ink2);background:#efece2;border-radius:8px;padding:8px 11px;margin-top:6px;line-height:1.7}
.reveal .jump{display:inline-block;margin-top:12px;font-size:14px;font-weight:700;text-decoration:none;
  border:1px solid var(--hanada);color:var(--hanada-d);border-radius:999px;padding:10px 18px}
.reveal .jump:active{background:var(--hanada);color:#fff}
.qbtns{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:18px}
.means.revq{max-width:440px;margin:10px auto 0;text-align:left}
.means.revq li{font-size:18.5px}
.qex{display:flex;gap:9px;align-items:flex-start;text-align:left;max-width:620px;margin:9px auto 0;font-size:16px;line-height:1.9}
.qexn,.rex .qexn{flex:none;width:1.5em;height:1.5em;border-radius:50%;background:#e7e2d4;color:var(--hanada-d);
  font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:.4em}
.qexko{flex:1}
.qexsrc{color:var(--ink3);font-size:11px;margin-left:5px}
.rex{display:flex;gap:9px;text-align:left;margin:12px auto 0;max-width:620px}
.rexbody{flex:1}
.reveal .ans.mincho{font-size:30px}
.qko .mk,.full .mk,.qextr .mk{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:4px;text-decoration-color:var(--suo);font-weight:600}
.qexlist{max-height:clamp(200px,40vh,380px);overflow-y:auto;-webkit-overflow-scrolling:touch;
  margin:8px auto 0;max-width:620px;border:1px solid #e3ddcf;border-radius:12px;background:#fbf9f3;padding:2px 6px}
.qex2{display:flex;gap:9px;align-items:flex-start;text-align:left;padding:10px 6px;border-top:1px solid #ece8dd}
.qex2:first-child{border-top:0}
.qexbody{flex:1;min-width:0}
.qexbody .qexko{font-size:16px;line-height:1.9}
.qextr{font-size:13.5px;color:var(--ink2);margin-top:4px;line-height:1.75}
.qb{font-family:inherit;font-size:16px;font-weight:700;border-radius:12px;padding:14px 22px;cursor:pointer;border:1px solid;flex:1 1 130px;max-width:220px}
.qb.show{background:var(--ink);color:#fff;border-color:var(--ink)}
.qb.know{background:var(--seiji);color:#fff;border-color:var(--seiji)}
.qb.again{background:#fff;color:var(--suo);border-color:var(--suo)}
.qdone{text-align:center}.qdone .big{font-family:'Shippori Mincho B1',serif;font-size:52px;color:var(--seiji);margin:10px 0}

@media (min-width:760px){
  .wrap{padding:0 18px}.controls{grid-template-columns:1fr auto;align-items:center}
  .controls .search{grid-column:1/-1}.brand small{font-size:12px}
  .qbtns .qb{flex:0 1 180px}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
:focus-visible{outline:2px solid var(--hanada);outline-offset:2px;border-radius:6px}
"""

HEAD = """<!doctype html><html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>%TITLE%</title>
<meta name="theme-color" content="#2f5670">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@500;600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap" rel="stylesheet">
<style>%CSS%</style></head><body>
<script>const DB=%DATA%;</script>
<script>if('serviceWorker' in navigator&&location.protocol.indexOf('http')===0)addEventListener('load',()=>navigator.serviceWorker.register('./sw.js').catch(()=>{}));</script>
"""

COLORS = r"""
const IMP_C={'最必修':'#8c414c','必修':'#2f5670','必修敬語':'#5f5480','重要':'#5f8472','応用':'#8a8276'};
const KEIGO_C={'尊敬':'#6f5f93','謙譲':'#3f6f86','丁寧':'#5f846f'};
const THEME_C={'恋・男女':'#8c5566','病・死・別れ':'#6c6f7a','仏道・信仰':'#7a6a45','宮廷・身分':'#5f5480',
'情趣':'#5f8472','時・時間':'#6f7a5a','ことば・学問':'#7a6480','思考・評判':'#4f6b86',
'プラスの評価・心情':'#3f6f86','マイナスの評価・心情':'#8a5a3f'};
const FLAG_C={'現代語とギャップ大':'#8c414c','現代語と少しズレ':'#b06a3a','多義語':'#2f5670','コアで覚える':'#3f6f86',
'漠然系':'#6a6275','プラス/マイナス両義':'#8a6d3f','呼応の副詞':'#5f5480','「〜なし」型':'#5f8472',
'漢語サ変':'#6c655a','敬語要注意':'#8c414c'};
function esc(s){return (s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function koUnder(s){return esc(s).replace(/\x01/g,'<u class="mk">').replace(/\x02/g,'</u>');}
function blankify(s){return esc(s).replace(/〔[\s　]*[〕\]）]/g,'<span class="blank">〔　　　〕</span>');}
function koRed(s){return esc(s).replace(/\x01/g,'<span class="exred">').replace(/\x02/g,'</span>');}
function ykMask(yb,imi){return esc(yb).replace(/〔[\s　]*[〕\]）]/g,'<span class="exmask" onclick="this.classList.toggle(\'open\')" tabindex="0">'+esc(imi)+'</span>');}
/* 覚えたチェックは意味ごと。キーは "番号:意味番号"（意味番号は1始まり、意味リストの順）。
   旧データ（番号だけの配列＝語単位）はその語の全意味を覚えた扱いに移行する。 */
const known=(()=>{const s=new Set();let raw=[];
  try{raw=JSON.parse(localStorage.getItem('koten_known')||'[]');}catch(e){}
  raw.forEach(v=>{const str=String(v);
    if(str.indexOf(':')>=0){s.add(str);}
    else{const w=DB.words.find(x=>x.no===+str);const n=w?(w.meanings.length||1):1;
      for(let i=1;i<=n;i++)s.add(str+':'+i);}});
  return s;})();
/* チェック日時（SRS-lite）。キーごとに epoch ms。日付の無い既存キーは移行時に現在時刻を入れる */
const knownAt=(()=>{let o={};try{o=JSON.parse(localStorage.getItem('koten_known_at')||'{}')||{}}catch(e){}
  const now=Date.now();known.forEach(k=>{if(!o[k])o[k]=now;});
  Object.keys(o).forEach(k=>{if(!known.has(k))delete o[k];});
  return o;})();
function saveKnown(){try{localStorage.setItem('koten_known',JSON.stringify([...known]));
  localStorage.setItem('koten_known_at',JSON.stringify(knownAt));}catch(e){}}
function addKnown(key){known.add(key);knownAt[key]=Date.now();}
function delKnown(key){known.delete(key);delete knownAt[key];}
/* あいまい（弱点）語の永続化。番号の配列 */
const weakSet=new Set((()=>{try{return JSON.parse(localStorage.getItem('koten_weak')||'[]')}catch(e){return[]}})());
function saveWeak(){try{localStorage.setItem('koten_weak',JSON.stringify([...weakSet]))}catch(e){}}
/* 復習期限：チェックから30日経過した既習意味は「復習待ち」 */
const DUE_MS=30*24*3600*1000;
function senseDue(key){return known.has(key)&&(Date.now()-(knownAt[key]||0))>DUE_MS;}
function wordDue(w){for(let i=1;i<=totalSenses(w);i++)if(senseDue(sk(w.no,i)))return true;return false;}
function reviewWords(){return DB.words.filter(w=>weakSet.has(w.no)||wordDue(w));}
/* 出典→成立時代（例文の出典表示に併記）。「源氏物語・松風」のような枝番は本体名で引く */
const SRC_ERA={'万葉集':'奈良','古事記':'奈良',
 '竹取物語':'平安前期','伊勢物語':'平安前期','古今和歌集':'平安前期','土佐日記':'平安前期',
 '後撰和歌集':'平安中期','平中物語':'平安中期','大和物語':'平安中期','蜻蛉日記':'平安中期',
 'うつほ物語':'平安中期','宇津保物語':'平安中期','落窪物語':'平安中期','枕草子':'平安中期',
 '源氏物語':'平安中期','和泉式部日記':'平安中期','紫式部日記':'平安中期','拾遺和歌集':'平安中期',
 '更級日記':'平安中期',
 '後拾遺和歌集':'平安後期','堤中納言物語':'平安後期','夜の寝覚':'平安後期','浜松中納言物語':'平安後期',
 '栄花物語':'平安後期','大鏡':'平安後期','今昔物語集':'平安後期','讃岐典侍日記':'平安後期',
 '詞花和歌集':'平安後期','梁塵秘抄':'平安末期','千載和歌集':'平安末期','今鏡':'平安末期',
 '住吉物語':'鎌倉前期','新古今和歌集':'鎌倉前期','方丈記':'鎌倉前期','無名抄':'鎌倉前期',
 '建礼門院右京大夫集':'鎌倉前期','平家物語':'鎌倉前期','平治物語':'鎌倉前期','宇治拾遺物語':'鎌倉前期',
 '古本説話集':'鎌倉前期','今物語':'鎌倉前期','十訓抄':'鎌倉中期','古今著聞集':'鎌倉中期',
 '十六夜日記':'鎌倉後期','沙石集':'鎌倉後期','玉葉和歌集':'鎌倉後期','徒然草':'鎌倉末期',
 '増鏡':'南北朝','太平記':'南北朝','義経記':'室町','閑吟集':'室町','文正草子':'室町',
 '唐糸草子':'室町','二十四孝':'室町','伊曾保物語':'江戸前期','野ざらし紀行':'江戸前期',
 '奥の細道':'江戸前期','折たく柴の記':'江戸中期','春雨物語':'江戸後期'};
function srcEra(s){if(!s)return'';return SRC_ERA[s]||SRC_ERA[s.split('・')[0]]||'';}
function srcLine(s){if(!s)return'—';const e=srcEra(s);return esc(s)+(e?'（'+e+'）':'');}
/* 検索用の仮名正規化：カタカナ→ひらがな、歴史的仮名（ゐゑを・ぢづ）を現代仮名に寄せる */
function normQ(s){return (s||'').toLowerCase()
  .replace(/[ァ-ヶ]/g,c=>String.fromCharCode(c.charCodeAt(0)-0x60))
  .replace(/[ゐ]/g,'い').replace(/[ゑ]/g,'え').replace(/を/g,'お')
  .replace(/ぢ/g,'じ').replace(/づ/g,'ず').replace(/[〜～]/g,'');}
function sk(no,i){return no+':'+i;}
function totalSenses(w){return w.meanings.length||1;}
function knownCount(w){let c=0;for(let i=1;i<=totalSenses(w);i++)if(known.has(sk(w.no,i)))c++;return c;}
function wordFull(w){return knownCount(w)===totalSenses(w);}
function masteredCount(){return DB.words.filter(wordFull).length;}
/* 意味ごとのチェックリスト（辞典カード／クイズの答え表示で共用）。tested=強調する意味番号(なければ0) */
function senseChecklist(w,tested){const multi=w.meanings.length>1;
  return `<ul class="mlist">`+w.meanings.map((m,k)=>{const i=k+1,on=known.has(sk(w.no,i)),t=tested===i;
    const face=on?'✓':(multi?String(i):'');
    return `<li class="mrow${on?' on':''}${t?' tested':''}">`
      +`<button class="mchk" data-no="${w.no}" data-si="${i}" aria-pressed="${on}" aria-label="この意味を覚えた（${esc(m)}）">${face}</button>`
      +`<span class="mtext">${esc(m)}${t?'<span class="testedtag">この問題の意味</span>':''}</span></li>`;}).join('')+`</ul>`;}
/* .mchk のクリックを配線。cb(no,i,now) は状態変更後に呼ばれる */
function bindSenseChecks(root,cb){root.querySelectorAll('.mchk').forEach(b=>b.onclick=()=>{
  const no=+b.dataset.no,i=+b.dataset.si,key=sk(no,i),now=!known.has(key);
  now?addKnown(key):delKnown(key);saveKnown();
  const w=DB.words.find(x=>x.no===no),multi=w&&w.meanings.length>1;
  b.setAttribute('aria-pressed',now);b.textContent=now?'✓':(multi?String(i):'');
  b.closest('.mrow').classList.toggle('on',now);
  if(cb)cb(no,i,now);});}
"""

INDEX_BODY = r"""
<header class="topbar"><div class="wrap row">
  <div class="brand"><span class="seal mincho">古</span><span>古文単語帳</span><small id="subtitle"></small></div>
  <nav class="topnav"><a class="btnlink solid" href="quiz.html">暗記テスト</a></nav>
</div></header>
<div class="wrap">
  <div class="controls">
    <label class="search">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="単語・意味で検索" autocomplete="off"></label>
    <div class="ctlrow">
      <button class="minibtn" id="tf">絞り込み</button>
      <select id="sort"><option value="no">番号順</option><option value="kana">五十音順</option><option value="pos">品詞順</option></select>
      <select id="view"><option value="all">すべて</option><option value="unknown">未習のみ</option><option value="known">既習のみ</option></select>
      <button class="minibtn" id="report">レポート</button>
      <span class="count" id="count"></span>
    </div>
  </div>
  <aside class="filters" id="filters" hidden></aside>
  <main class="list" id="list"></main>
</div>
<div class="modal" id="noteModal" hidden><div class="modal-card" role="dialog" aria-modal="true" aria-labelledby="noteTitle">
  <button class="modal-x" id="noteClose" aria-label="閉じる">×</button>
  <div class="modal-eyebrow">覚え方の解説</div>
  <div class="modal-title" id="noteTitle"></div>
  <div class="modal-sub" id="noteSub"></div>
  <div class="modal-body" id="noteBody"></div>
</div></div>
<div class="modal" id="repModal" hidden><div class="modal-card" role="dialog" aria-modal="true">
  <button class="modal-x" id="repClose" aria-label="閉じる">×</button>
  <div class="modal-eyebrow">学習レポート</div>
  <div class="modal-body" id="repBody"></div>
</div></div>
<script>
%COLORS%
const $=s=>document.querySelector(s);
$('#subtitle').textContent='全'+DB.meta.total+'語・タップで詳しく';
const state={q:'',sort:'no',view:'all',sel:{imp:new Set(),pos:new Set(),keigo:new Set(),theme:new Set(),flag:new Set()}};
const FACETS=[['imp','重要度',DB.meta.imp,IMP_C],['pos','品詞',DB.meta.pos,null],
 ['keigo','敬語',DB.meta.keigo,KEIGO_C],['theme','意味テーマ',DB.meta.theme,THEME_C],['flag','覚え方',DB.meta.flag,FLAG_C]];
function buildFilters(){
  let h='<div class="filterbar"><span>タグで絞り込み（観点ごと複数可・観点間はAND）</span><button class="clear" id="clr">解除</button></div>';
  for(const [key,label,vals,cmap] of FACETS){h+=`<div class="facet"><h4>${label}</h4><div class="chips">`;
    for(const v of vals){const c=cmap?cmap[v]:'#7a7264';
      h+=`<button class="chip" data-f="${key}" data-v="${esc(v)}" style="--c:${c}">${esc(v)}</button>`;}h+='</div></div>';}
  $('#filters').innerHTML=h;
  $('#filters').querySelectorAll('.chip').forEach(ch=>ch.onclick=()=>{
    const f=ch.dataset.f,v=ch.dataset.v;state.sel[f].has(v)?state.sel[f].delete(v):state.sel[f].add(v);
    ch.classList.toggle('on');render();});
  $('#clr').onclick=clearFilters;
}
function clearFilters(){for(const k in state.sel)state.sel[k].clear();
  $('#filters').querySelectorAll('.chip.on').forEach(c=>c.classList.remove('on'));render();}
function setChip(f,v){state.sel[f].add(v);
  $('#filters').querySelectorAll('.chip[data-f="'+f+'"]').forEach(ch=>{if(ch.dataset.v===v)ch.classList.add('on');});
  if($('#filters').hidden){$('#filters').hidden=false;$('#tf').classList.add('act');}
  render();window.scrollTo({top:0,behavior:'smooth'});}
function relJump(no){clearFilters();state.q='';$('#q').value='';state.view='all';$('#view').value='all';render();
  const el=$('#w'+no);if(el){if(el.scrollIntoView)el.scrollIntoView({behavior:'smooth',block:'center'});el.classList.remove('flash');void el.offsetWidth;el.classList.add('flash');}}
function match(w){const s=state.sel;
  if(state.view==='unknown'&&wordFull(w))return false;
  if(state.view==='known'&&!wordFull(w))return false;
  if(s.imp.size&&!s.imp.has(w.imp))return false;
  if(s.pos.size&&!s.pos.has(w.pos))return false;
  if(s.keigo.size&&!w.keigo.some(k=>s.keigo.has(k)))return false;
  if(s.theme.size&&!w.themes.some(t=>s.theme.has(t)))return false;
  if(s.flag.size&&!w.flags.some(t=>s.flag.has(t)))return false;
  if(state.q){const q=normQ(state.q);
    if(w._hay===undefined)w._hay=normQ(w.word+' '+(w.kanji||'')+' '+w.meanings.join(' ')+' '+w.themes.join(' ')+' '+w.flags.join(' '));
    if(!w._hay.includes(q))return false;}
  return true;}
const POSORD=DB.meta.pos;
function sortList(a){
  if(state.sort==='kana')return a.sort((x,y)=>x.word.localeCompare(y.word,'ja')||x.no-y.no);
  if(state.sort==='pos')return a.sort((x,y)=>POSORD.indexOf(x.pos)-POSORD.indexOf(y.pos)||x.no-y.no);
  return a.sort((x,y)=>x.no-y.no);}
function relInner(w){
  const order={};w.related.forEach(r=>{(order[r.sense]=order[r.sense]||[]).push(r);});
  let h='<div class="rellabel">関連語・混同注意（訳ごと）</div>';
  for(const sense in order){h+=`<div class="relgroup"><span class="relsense">${esc(sense)}</span>`;
    ['類義','対義','混同'].forEach(t=>{const it=order[sense].filter(r=>r.type===t);
      if(it.length){h+=`<span class="reltype rt-${t}">${t}</span>`+
        it.map(r=>`<button class="relw" data-no="${r.no}">${esc(r.word)}<small>${esc(r.gloss)}</small></button>`).join('');}});h+='</div>';}
  return h;}
function card(w){
  const kc=knownCount(w),tot=totalSenses(w),full=kc===tot;
  const meta=`<span class="pos">${esc(w.pos)}</span>`+(w.kat?`<span class="kat">${esc(w.kat)}</span>`:'')
    +w.keigo.map(k=>`<span class="kg" style="--c:${KEIGO_C[k]}">${esc(k)}</span>`).join('')
    +w.themes.map(t=>`<button class="tag th" data-f="theme" data-v="${esc(t)}" style="--c:${THEME_C[t]}">${esc(t)}</button>`).join('')
    +w.flags.map(t=>`<button class="tag flag" data-f="flag" data-v="${esc(t)}" style="--c:${FLAG_C[t]}">${esc(t)}</button>`).join('');
  const means=senseChecklist(w,0);
  const exN=w.examples.length, relN=(w.related||[]).length;
  const ex=w.examples.map(e=>`<div class="ex">
    <div class="ko mincho">${koRed(e.koU)}</div>
    <div class="yk">${ykMask(e.ykBlank,e.imi)}</div>
    <div class="src">出典：${srcLine(e.src)}</div></div>`).join('');
  return `<article class="card${full?' learned':''}" id="w${w.no}" style="--impc:${IMP_C[w.imp]}">
    <div class="ctop">
      <button class="known${kc&&!full?' partial':''}" data-no="${w.no}" aria-pressed="${full}" aria-label="すべての意味を覚えた" title="全${tot}中 ${kc} 覚えた">${full?'✓':(kc||'')}</button>
      <div class="hwblock">
        <div class="hwline"><span class="no">${w.no}</span><span class="word mincho">${esc(w.word)}</span>${w.kanji?`<span class="kanji">〔${esc(w.kanji)}〕</span>`:''}
          <span class="imp" style="color:${IMP_C[w.imp]}">${esc(w.imp)}</span></div>
        <div class="metaline">${meta}</div>
      </div>
    </div>
    <div class="body2">${means}${w.note?`<button class="noteprev" data-no="${w.no}"><span class="lbl">覚え方の解説<span class="more">タップで全文 →</span></span><span class="snip">${esc(w.note)}</span></button>`:''}</div>
    <div class="discl">
      <button class="disc" data-t="ex">例文 ${exN} ▾</button>
      ${relN?`<button class="disc" data-t="rel">関連・混同 ${relN} ▾</button>`:''}
    </div>
    <div class="panel" data-p="ex">${ex}</div>
    ${relN?`<div class="panel" data-p="rel">${relInner(w)}</div>`:''}
  </article>`;}
function setCount(shown){$('#count').innerHTML=`${shown} 語　<b>既習 ${masteredCount()}</b>`;}
function paintMaster(cardEl,w){const kc=knownCount(w),tot=totalSenses(w),full=kc===tot;
  cardEl.classList.toggle('learned',full);
  const c=cardEl.querySelector('.known');
  c.setAttribute('aria-pressed',full);c.classList.toggle('partial',kc>0&&!full);
  c.textContent=full?'✓':(kc||'');c.title=`全${tot}中 ${kc} 覚えた`;}
function render(){
  let arr=DB.words.filter(match);sortList(arr);
  setCount(arr.length);
  const L=$('#list');
  if(!arr.length){L.innerHTML='<div class="empty">該当する単語がありません。<br>検索語やタグ・表示条件を見直してください。</div>';return;}
  L.innerHTML=arr.map(card).join('');
  L.querySelectorAll('.disc:not(.note)').forEach(b=>b.onclick=()=>{
    const p=b.parentElement.parentElement.querySelector('.panel[data-p="'+b.dataset.t+'"]');
    const open=p.classList.toggle('open');b.classList.toggle('open',open);
    b.textContent=b.textContent.replace(/[▾▴]/,open?'▴':'▾');});
  L.querySelectorAll('.noteprev').forEach(b=>b.onclick=()=>openNote(+b.dataset.no));
  L.querySelectorAll('.tag').forEach(t=>t.onclick=()=>setChip(t.dataset.f,t.dataset.v));
  L.querySelectorAll('.relw').forEach(r=>r.onclick=()=>relJump(r.dataset.no));
  bindSenseChecks(L,no=>{const cardEl=L.querySelector('#w'+no);
    if(cardEl)paintMaster(cardEl,DB.words.find(x=>x.no===no));
    setCount(L.querySelectorAll('.card').length);
    if(state.view!=='all')render();});
  L.querySelectorAll('.known').forEach(k=>k.onclick=()=>{
    const no=+k.dataset.no,w=DB.words.find(x=>x.no===no),full=wordFull(w);
    for(let i=1;i<=totalSenses(w);i++){const key=sk(no,i);full?delKnown(key):addKnown(key);}
    saveKnown();
    const cardEl=k.closest('.card');
    cardEl.querySelectorAll('.mchk').forEach(b=>{const on=known.has(sk(no,+b.dataset.si));
      b.setAttribute('aria-pressed',on);b.textContent=on?'✓':(w.meanings.length>1?b.dataset.si:'');
      b.closest('.mrow').classList.toggle('on',on);});
    paintMaster(cardEl,w);setCount(L.querySelectorAll('.card').length);
    if(state.view!=='all')render();});
  if(location.hash){const el=document.querySelector(location.hash);
    if(el){if(el.scrollIntoView)el.scrollIntoView({behavior:'smooth',block:'center'});el.classList.add('flash');}}}
let _qT;$('#q').oninput=e=>{const v=e.target.value;clearTimeout(_qT);
  _qT=setTimeout(()=>{state.q=v.trim();render();},150);};
$('#sort').onchange=e=>{state.sort=e.target.value;render();};
$('#view').onchange=e=>{state.view=e.target.value;render();};
$('#tf').onclick=()=>{const f=$('#filters');f.hidden=!f.hidden;$('#tf').classList.toggle('act',!f.hidden);};
function openNote(no){const w=DB.words.find(x=>x.no===no);if(!w)return;
  $('#noteTitle').innerHTML=`<span class="mincho">${esc(w.word)}</span>${w.kanji?`<span class="ktitle">〔${esc(w.kanji)}〕</span>`:''}`;
  $('#noteSub').innerHTML=`<span class="badge" style="background:${IMP_C[w.imp]}">${esc(w.imp)}</span>`
    +`<span class="badge" style="background:#7a7264">${esc(w.pos)}</span>`
    +(w.kat?`<span class="badge" style="background:#8a8276">${esc(w.kat)}</span>`:'')
    +w.keigo.map(k=>`<span class="badge" style="background:${KEIGO_C[k]}">${esc(k)}</span>`).join('')
    +`<span>${w.meanings.map(esc).join(' / ')}</span>`;
  $('#noteBody').textContent=w.note||'';
  const m=$('#noteModal');m.hidden=false;m.querySelector('.modal-card').scrollTop=0;document.body.style.overflow='hidden';}
function closeNote(){$('#noteModal').hidden=true;document.body.style.overflow='';}
$('#noteClose').onclick=closeNote;
$('#noteModal').onclick=e=>{if(e.target.id==='noteModal')closeNote();};
/* 学習レポート：重要度帯・テーマ別の既習率と弱点・復習期限切れの一覧 */
function repBar(label,k,n,color){const p=n?Math.round(k/n*100):0;
  return `<div class="rep"><span class="replabel">${esc(label)}</span><span class="repbar"><i style="width:${p}%;background:${color||'#7a7264'}"></i></span><span class="repnum">${k}/${n}</span></div>`;}
function openReport(){
  const senseTot=DB.words.reduce((a,w)=>a+totalSenses(w),0);
  let h=`<div class="repline">既習：<b>${masteredCount()}</b> / ${DB.words.length} 語（意味単位 <b>${known.size}</b> / ${senseTot}）</div>`;
  h+='<h4>重要度別（全意味を覚えた語）</h4>';
  DB.meta.imp.forEach(b=>{const ws=DB.words.filter(w=>w.imp===b);if(!ws.length)return;
    h+=repBar(b,ws.filter(wordFull).length,ws.length,IMP_C[b]);});
  h+='<h4>テーマ別（全意味を覚えた語）</h4>';
  DB.meta.theme.forEach(t=>{const ws=DB.words.filter(w=>w.themes.includes(t));if(!ws.length)return;
    h+=repBar(t,ws.filter(wordFull).length,ws.length,THEME_C[t]);});
  const wk=[...weakSet].map(no=>DB.words.find(w=>w.no===no)).filter(Boolean).sort((a,b)=>a.no-b.no);
  h+=`<h4>あいまい（弱点）：${wk.length}語</h4>`;
  h+=wk.length?`<div class="repweak">${wk.map(w=>`<button class="relw" data-no="${w.no}">${esc(w.word)}</button>`).join('')}</div>`:'<p class="help">なし。テストで「あいまい」にした語がここに並びます。</p>';
  const due=DB.words.filter(wordDue);
  h+=`<h4>復習期限切れ（チェックから30日）：${due.length}語</h4>`;
  h+=due.length?`<div class="repweak">${due.map(w=>`<button class="relw" data-no="${w.no}">${esc(w.word)}</button>`).join('')}</div>`:'<p class="help">なし。</p>';
  $('#repBody').innerHTML=h;
  $('#repBody').querySelectorAll('.relw').forEach(b=>b.onclick=()=>{closeReport();relJump(+b.dataset.no);});
  const m=$('#repModal');m.hidden=false;m.querySelector('.modal-card').scrollTop=0;document.body.style.overflow='hidden';}
function closeReport(){$('#repModal').hidden=true;document.body.style.overflow='';}
$('#report').onclick=openReport;
$('#repClose').onclick=closeReport;
$('#repModal').onclick=e=>{if(e.target.id==='repModal')closeReport();};
document.addEventListener('keydown',e=>{if(e.key!=='Escape')return;
  if(!$('#noteModal').hidden)closeNote();if(!$('#repModal').hidden)closeReport();});
buildFilters();render();window.addEventListener('hashchange',render);
</script>
"""

QUIZ_BODY = r"""
<header class="topbar"><div class="wrap row">
  <div class="brand"><span class="seal mincho">試</span><span>暗記テスト</span><small>答え合わせで辞典へ</small></div>
  <nav class="topnav"><a class="btnlink" href="index.html">辞典</a></nav>
</div></header>
<div class="wrap">
  <section class="qsetup" id="setup">
    <h2>テスト設定</h2><p class="help">向き・範囲・問題数・順番をえらんで「はじめる」。</p>
    <div class="field"><h4>出題の向き</h4><div class="modebtns" id="modebtns">
      <button class="modebtn on" data-m="fwd"><b>単語 → 意味</b><span>古語と例文を見て意味を答える</span></button>
      <button class="modebtn" data-m="rev"><b>意味 → 単語（逆引き）</b><span>現代語訳を見て古語を答える</span></button>
      <button class="modebtn" data-m="mc"><b>四択テスト</b><span>正しい意味を四つの選択肢から選ぶ</span></button>
    </div></div>
    <div class="field"><h4>重要度（未選択ですべて）</h4><div class="chips" id="fImp"></div></div>
    <div class="field"><h4>品詞（任意）</h4><div class="chips" id="fPos"></div></div>
    <div class="field"><h4>意味テーマ（任意）</h4><div class="chips" id="fTheme"></div></div>
    <div class="field"><h4>覚え方タグ（任意）</h4><div class="chips" id="fFlag"></div></div>
    <div class="field"><div class="row">
      <div><h4 style="margin:0 0 6px">問題数</h4>
        <select id="num"><option value="10">10問</option><option value="20">20問</option><option value="30">30問</option><option value="50">50問</option><option value="0">範囲すべて</option></select></div>
      <div><h4 style="margin:0 0 6px">順番</h4>
        <select id="order"><option value="shuffle">ランダム</option><option value="no">番号順</option></select></div>
      <div style="margin-left:auto;text-align:right"><div class="bignum" id="pcount">0</div>
        <div style="font-size:11px;color:var(--ink2)">範囲の語数</div></div>
    </div></div>
    <div class="field reviewbox" id="reviewBox" hidden><h4>復習キュー</h4>
      <div class="row" style="align-items:center;gap:10px">
        <span class="reviewinfo" id="reviewInfo"></span>
        <button class="minibtn" id="reviewStart" style="margin-left:auto;min-height:44px">復習キューで始める</button>
      </div>
      <p class="help" style="margin:6px 0 0">「あいまい」にした語と、覚えたチェックから30日たった語をまとめて出題します。</p>
    </div>
    <div style="text-align:center;margin-top:6px"><button class="start" id="startBtn">はじめる</button></div>
  </section>

  <section class="qplay" id="play" hidden>
    <div class="qmeta"><span id="pos">1 / 1</span><span id="kn">覚えた 0</span>
      <button class="minibtn" id="quit" style="margin-left:auto;min-height:36px">設定</button></div>
    <div class="progress"><i id="bar" style="width:0%"></i></div>
    <div class="qcard">
      <div class="qbadge" id="qbadge"></div>
      <div id="qhead"></div>
      <div class="qprompt" id="qprompt"></div>
      <div id="qbody"></div>
      <div class="reveal" id="reveal"></div>
      <div class="qbtns" id="btns"></div>
    </div>
  </section>

  <section class="qdone" id="done" hidden>
    <div class="big mincho" id="score">0 / 0</div>
    <p id="donemsg" style="color:var(--ink2)"></p>
    <div class="qbtns">
      <button class="qb know" id="againAll">もう一度</button>
      <button class="qb again" id="reviewWeak">あいまい復習</button>
      <button class="qb show" id="back">設定にもどる</button>
    </div>
  </section>
</div>
<script>
%COLORS%
const $=s=>document.querySelector(s);
let mode='fwd';const sel={imp:new Set(),pos:new Set(),theme:new Set(),flag:new Set()};
function chips(host,vals,cmap,key){
  host.innerHTML=vals.map(v=>`<button class="chip" data-v="${esc(v)}" style="--c:${cmap?cmap[v]:'#7a7264'}">${esc(v)}</button>`).join('');
  host.querySelectorAll('.chip').forEach(ch=>ch.onclick=()=>{const v=ch.dataset.v;
    sel[key].has(v)?sel[key].delete(v):sel[key].add(v);ch.classList.toggle('on');updateCount();});}
chips($('#fImp'),DB.meta.imp,IMP_C,'imp');chips($('#fPos'),DB.meta.pos,null,'pos');
chips($('#fTheme'),DB.meta.theme,THEME_C,'theme');chips($('#fFlag'),DB.meta.flag,FLAG_C,'flag');
$('#modebtns').querySelectorAll('.modebtn').forEach(b=>b.onclick=()=>{
  mode=b.dataset.m;$('#modebtns').querySelectorAll('.modebtn').forEach(x=>x.classList.toggle('on',x===b));});
function pool(){return DB.words.filter(w=>{
  if(sel.imp.size&&!sel.imp.has(w.imp))return false;
  if(sel.pos.size&&!sel.pos.has(w.pos))return false;
  if(sel.theme.size&&!w.themes.some(t=>sel.theme.has(t)))return false;
  if(sel.flag.size&&!w.flags.some(t=>sel.flag.has(t)))return false;return true;});}
function updateCount(){const n=pool().length;$('#pcount').textContent=n;$('#startBtn').disabled=n===0;updateReview();}
function updateReview(){const rw=reviewWords();
  $('#reviewBox').hidden=rw.length===0;
  if(!rw.length)return;
  const nW=rw.filter(w=>weakSet.has(w.no)).length;
  $('#reviewInfo').textContent=`${rw.length}語（あいまい ${nW}・期限切れ ${rw.length-nW}）`;}
$('#reviewStart').onclick=()=>{const rw=reviewWords();if(rw.length)start(rw);};
updateCount();
let deck=[],idx=0,knownRun=0,weak=[];
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]];}return a;}
function start(list){deck=list.slice();
  if($('#order').value==='shuffle')shuffle(deck);else deck.sort((a,b)=>a.no-b.no);
  const n=parseInt($('#num').value,10);if(n>0)deck=deck.slice(0,n);
  idx=0;knownRun=0;weak=[];$('#setup').hidden=true;$('#done').hidden=true;$('#play').hidden=false;show();}
const BLK=/〔[\s　]*[〕\]）]/g;
function ykUnder(yb,imi){return esc(yb).replace(/〔[\s　]*[〕\]）]/g,`<u class="mk">${esc(imi)}</u>`);}
let cur={};
function badge(t,c,cls){return `<span class="${cls}" style="background:${c}">${esc(t)}</span>`;}
function meansList(w,cls){
  if(w.meanings.length<=1)return `<div class="means one ${cls||''}">${esc(w.meanings[0]||'')}</div>`;
  return `<ol class="means ${cls||''}">${w.meanings.map(m=>`<li>${esc(m)}</li>`).join('')}</ol>`;}
function midx(w,imi){const i=w.meanings.indexOf(imi);return i>=0?i+1:0;}
/* ---- 四択：誤答肢の自動生成 ----
   優先度＝混同語 > 対義語 > 同テーマ・同品詞 > 同品詞 > 全語。
   自語の意味と語義片（・区切り）が重なる候補は除外（正解が複数になるのを防ぐ） */
function mcFrags(s){return (s||'').replace(/[（(][^（）()]*[）)]/g,'').split(/[・／\/]/).filter(x=>x);}
function mcConflict(a,b){const A=new Set(mcFrags(a));return mcFrags(b).some(f=>A.has(f));}
function mcBuild(w,correct){
  const chosen=[correct];
  const bad=c=>!c||chosen.some(x=>x===c||mcConflict(x,c))||w.meanings.some(m=>mcConflict(m,c));
  const nos=[];
  (w.related||[]).forEach(r=>{if(r.type==='混同')nos.push(r.no);});
  (w.related||[]).forEach(r=>{if(r.type==='対義')nos.push(r.no);});
  const th=new Set(w.themes);
  nos.push(...shuffle(DB.words.filter(x=>x.no!==w.no&&x.pos===w.pos&&x.themes.some(t=>th.has(t))).map(x=>x.no)));
  nos.push(...shuffle(DB.words.filter(x=>x.no!==w.no&&x.pos===w.pos).map(x=>x.no)));
  nos.push(...shuffle(DB.words.filter(x=>x.no!==w.no).map(x=>x.no)));
  for(const no of nos){if(chosen.length>=4)break;
    const cw=DB.words.find(x=>x.no===no);
    const c=cw.meanings[Math.random()*cw.meanings.length|0];
    if(!bad(c))chosen.push(c);}
  return shuffle(chosen.map((t,i)=>({t,ok:i===0})));}
function mcAnswer(btn){const w=cur.w,e=cur.e;
  if($('#qbody').dataset.done)return;$('#qbody').dataset.done='1';
  $('#qbody').querySelectorAll('.mcbtn').forEach(b=>{
    if(b.dataset.ok==='1')b.classList.add('ok');else if(b===btn)b.classList.add('ng');
    b.disabled=true;});
  $('#reveal').innerHTML=`<div class="qkolabel">意味（覚えたらチェック）</div>`+senseChecklist(w,e.mi||0)
    +`<div class="tr">訳：${esc((e.yk||'').replace(BLK,e.imi))}</div>`
    +`<a class="jump" href="index.html#w${w.no}">辞典で詳しく確認 →</a>`;
  $('#reveal').classList.add('show');bindSenseChecks($('#reveal'));
  /* 記録は他モードと同じ自己判定（覚えた／あいまい）で統一 */
  $('#btns').innerHTML='<button class="qb again" id="againBtn">あいまい</button><button class="qb know" id="knowBtn">覚えた</button>';
  $('#againBtn').onclick=()=>{weak.push(w);weakSet.add(w.no);saveWeak();next();};
  $('#knowBtn').onclick=()=>{const i=e.mi||(w.meanings.length<=1?1:0);
    if(i)addKnown(sk(w.no,i));else for(let k=1;k<=totalSenses(w);k++)addKnown(sk(w.no,k));
    saveKnown();weakSet.delete(w.no);saveWeak();knownRun++;next();};}
function allCloze(w){return w.examples.map(e=>{const n=midx(w,e.imi);
  return `<div class="qex"><span class="qexn">${n||'・'}</span><span class="qexko mincho">${blankify(e.koBlank)}${e.src?`<span class="qexsrc">（${esc(e.src)}）</span>`:''}</span></div>`;}).join('');}
function show(){const w=deck[idx];cur.w=w;const e=w.examples[Math.random()*w.examples.length|0];cur.e=e;
  $('#pos').textContent=`${idx+1} / ${deck.length}`;$('#kn').textContent=`覚えた ${knownRun}`;
  $('#bar').style.width=(idx/deck.length*100)+'%';
  $('#qbadge').innerHTML=badge(w.imp,IMP_C[w.imp],'imp2')+badge(w.pos,'#7a7264','pos')
    +(w.kat?badge(w.kat,'#8a8276','pos'):'')+w.keigo.map(k=>badge(k,KEIGO_C[k],'kg')).join('');
  $('#reveal').classList.remove('show');$('#reveal').innerHTML='';
  if(mode==='mc'){
    delete $('#qbody').dataset.done;
    $('#qhead').innerHTML=`<div class="qword mincho">${esc(w.word)}</div>`;
    $('#qprompt').textContent='この語の意味は？（四択）';
    const correct=(e.mi&&w.meanings[e.mi-1])||w.meanings[0];
    const ch=mcBuild(w,correct);
    $('#qbody').innerHTML=`<div class="qkolabel">例文（古文）</div><div class="qko mincho">${koUnder(e.koU)}</div>`
      +`${e.src?`<div class="qsrc">出典：${srcLine(e.src)}</div>`:''}`
      +`<button class="hintbtn" id="hintBtn">ヒント（訳）を見る ▾</button>`
      +`<div class="qhintlabel" id="qhintlabel" style="display:none">訳（問われている語が空欄）</div>`
      +`<div class="qhint" id="qhint" style="display:none">${blankify(e.ykBlank)}</div>`
      +`<div class="mcgrid">`+ch.map((c,i)=>`<button class="mcbtn" data-ok="${c.ok?1:0}"><span class="mck">${'アイウエ'[i]}</span>${esc(c.t)}</button>`).join('')+`</div>`;
    $('#hintBtn').onclick=()=>{const h=$('#qhint'),l=$('#qhintlabel'),o=h.style.display==='none';
      h.style.display=o?'':'none';l.style.display=o?'':'none';
      $('#hintBtn').textContent=o?'ヒント（訳）を隠す ▴':'ヒント（訳）を見る ▾';};
    $('#qbody').querySelectorAll('.mcbtn').forEach(b=>b.onclick=()=>mcAnswer(b));
    $('#btns').innerHTML='';
    return;}
  if(mode==='fwd'){
    $('#qhead').innerHTML=`<div class="qword mincho">${esc(w.word)}</div>`;
    $('#qprompt').textContent='この語の意味は？';
    $('#qbody').innerHTML=`<div class="qkolabel">例文（古文）</div><div class="qko mincho">${koUnder(e.koU)}</div>`
      +`${e.src?`<div class="qsrc">出典：${srcLine(e.src)}</div>`:''}`
      +`<button class="hintbtn" id="hintBtn">ヒント（訳）を見る ▾</button>`
      +`<div class="qhintlabel" id="qhintlabel" style="display:none">訳（同じ箇所が空欄）</div>`
      +`<div class="qhint" id="qhint" style="display:none">${blankify(e.ykBlank)}</div>`;
    $('#hintBtn').onclick=()=>{const h=$('#qhint'),l=$('#qhintlabel'),o=h.style.display==='none';
      h.style.display=o?'':'none';l.style.display=o?'':'none';
      $('#hintBtn').textContent=o?'ヒント（訳）を隠す ▴':'ヒント（訳）を見る ▾';};
  }else{
    $('#qhead').innerHTML=`<div class="qkolabel">次の意味を表す古語は？</div>${meansList(w,'revq')}`;
    $('#qprompt').textContent='';
    $('#qbody').innerHTML=`<div class="qkolabel">例文（空欄に入る古語を答える／下線は訳のヒント）</div>`
      +`<div class="qexlist">`+w.examples.map(e=>`<div class="qex2"><span class="qexn">${w.meanings.length>1?(e.mi||'・'):'・'}</span>`
        +`<div class="qexbody"><div class="qexko mincho">${blankify(e.koBlank)}${e.src?`<span class="qexsrc">（${esc(e.src)}）</span>`:''}</div>`
        +`<div class="qextr">訳：${ykUnder(e.ykBlank,e.imi)}</div></div></div>`).join('')+`</div>`;}
  $('#btns').innerHTML='<button class="qb show" id="showBtn">答えを見る</button>';
  $('#showBtn').onclick=revealAns;}
function revealAns(){const w=cur.w,e=cur.e;let h='';
  if(mode==='fwd'){
    h=`<div class="qkolabel">意味（覚えたらチェック）</div>`+senseChecklist(w,cur.e.mi||0)
     +`<div class="tr">訳：${esc((e.yk||'').replace(BLK,e.imi))}</div>`;
  }else{
    h=`<div class="ans mincho">${esc(w.word)}</div>`
     +`<div class="qkolabel">意味（覚えたらチェック）</div>`+senseChecklist(w,0)
     +`<div class="qexlist">`+w.examples.map(ex=>`<div class="qex2"><span class="qexn">${w.meanings.length>1?(ex.mi||'・'):'・'}</span><div class="qexbody"><div class="full mincho">${koUnder(ex.koU)}</div><div class="qextr">${esc((ex.yk||'').replace(BLK,ex.imi))}</div></div></div>`).join('')+`</div>`;}
  h+=`<a class="jump" href="index.html#w${w.no}">辞典で詳しく確認 →</a>`;
  $('#reveal').innerHTML=h;$('#reveal').classList.add('show');
  bindSenseChecks($('#reveal'));
  $('#btns').innerHTML='<button class="qb again" id="againBtn">あいまい</button><button class="qb know" id="knowBtn">覚えた</button>';
  $('#againBtn').onclick=()=>{weak.push(w);weakSet.add(w.no);saveWeak();next();};
  $('#knowBtn').onclick=()=>{const w=cur.w;
    if(mode==='fwd'){const i=cur.e.mi||(w.meanings.length<=1?1:0);
      if(i)addKnown(sk(w.no,i));else for(let k=1;k<=totalSenses(w);k++)addKnown(sk(w.no,k));}
    else{for(let k=1;k<=totalSenses(w);k++)addKnown(sk(w.no,k));}
    saveKnown();weakSet.delete(w.no);saveWeak();knownRun++;next();};}
function next(){idx++;if(idx>=deck.length)finish();else show();}
function finish(){$('#play').hidden=true;$('#done').hidden=false;$('#bar').style.width='100%';
  $('#score').textContent=`${knownRun} / ${deck.length}`;
  $('#donemsg').textContent=weak.length?`「あいまい」が ${weak.length} 語。復習しましょう。`:'すべて「覚えた」！おみごと。';
  $('#reviewWeak').style.display=weak.length?'':'none';}
$('#startBtn').onclick=()=>start(pool());
$('#quit').onclick=()=>{$('#play').hidden=true;$('#setup').hidden=false;updateCount();};
$('#back').onclick=()=>{$('#done').hidden=true;$('#setup').hidden=false;updateCount();};
$('#againAll').onclick=()=>start(deck);$('#reviewWeak').onclick=()=>start(weak);
</script>
"""

def build(title,body):
    return HEAD.replace('%TITLE%',title).replace('%CSS%',CSS).replace('%DATA%',DATA)+body.replace('%COLORS%',COLORS)+"</body></html>"
open(os.path.join(ROOT,'dist','index.html'),'w',encoding='utf-8').write(build('古文単語帳｜辞典',INDEX_BODY))
open(os.path.join(ROOT,'dist','quiz.html'),'w',encoding='utf-8').write(build('古文単語帳｜暗記テスト',QUIZ_BODY))

# ---------- PWA（manifest / Service Worker / アイコン） ----------
import time, shutil, json as _json
MANIFEST={"name":"古文単語帳","short_name":"古文単語","start_url":"./","scope":"./",
 "display":"standalone","background_color":"#e4e0d3","theme_color":"#2f5670",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},
          {"src":"icon-512.png","sizes":"512x512","type":"image/png"},
          {"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]}
open(os.path.join(ROOT,'dist','manifest.webmanifest'),'w',encoding='utf-8').write(_json.dumps(MANIFEST,ensure_ascii=False))
# SW: ナビゲーションはネット優先（更新を取り込み、オフライン時はキャッシュ）。
# フォント（Google Fonts）と同一オリジンの静的物はキャッシュ優先＋裏で更新。
SW = r"""const V='koten-%STAMP%';
const CORE=['./','./quiz','./manifest.webmanifest','./icon-192.png','./icon-512.png','./apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V&&k!=='koten-rt').map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const req=e.request;if(req.method!=='GET')return;
  const u=new URL(req.url);
  if(req.mode==='navigate'){
    e.respondWith(fetch(req).then(r=>{const cp=r.clone();caches.open(V).then(c=>c.put(req,cp));return r;})
      .catch(()=>caches.match(req).then(r=>r||caches.match(u.pathname.indexOf('quiz')>=0?'./quiz':'./'))));
    return;}
  if(u.origin===location.origin||u.hostname==='fonts.googleapis.com'||u.hostname==='fonts.gstatic.com'){
    e.respondWith(caches.open('koten-rt').then(c=>c.match(req).then(hit=>{
      const net=fetch(req).then(r=>{if(r&&r.ok)c.put(req,r.clone());return r;}).catch(()=>hit);
      return hit||net;})));}
});
""".replace('%STAMP%',time.strftime('%Y%m%d%H%M%S'))
open(os.path.join(ROOT,'dist','sw.js'),'w',encoding='utf-8').write(SW)
ASSETS=os.path.join(ROOT,'assets')
if os.path.isdir(ASSETS):
    for fn in ['icon-192.png','icon-512.png','apple-touch-icon.png']:
        p=os.path.join(ASSETS,fn)
        if os.path.exists(p): shutil.copy2(p,os.path.join(ROOT,'dist',fn))

for fn in ['index.html','quiz.html']:print(fn,os.path.getsize(os.path.join(ROOT,'dist',fn))//1024,'KB')
print('pwa:',sorted(f for f in os.listdir(os.path.join(ROOT,'dist')) if not f.endswith('.html')))
