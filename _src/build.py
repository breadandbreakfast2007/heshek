# Builds the static preview pages. Run: python3 _src/build.py  (from repo root)
import os,re
R=os.path.dirname(os.path.abspath(__file__))
def part(n): return open(os.path.join(R,'parts_%s.html'%n),encoding='utf-8').read()
NAV=[('shop.html','חנות'),('how.html','איך מכינים'),('business.html','לעסקים ואירועים'),('story.html','הסיפור'),('contact.html','צרו קשר')]
def nav(active):
    return ''.join('<a href="%s"%s>%s</a>'%(h,' aria-current="page"' if h==active else '',t) for h,t in NAV)
LAYOUT='''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Suez+One&family=Assistant:wght@400;600;700&family=Karantina:wght@700&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">

<div class="draftbar"><div class="in">טיוטה לעיון. מה שמסומן ב<span class="todo" style="font-size:.75rem">להחלפה</span> מחכה לחומרים או לפרטים.</div></div>

<header>
  <div class="in">
    <div class="hdr-start">
      <button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="תפריט"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" fill="none"/></svg></button>
      <nav aria-label="ראשי">{nav}</nav>
    </div>
    <a class="logo" href="index.html" aria-label="חשק, חברה של קפה, לעמוד הבית"><img src="img/logo.svg" alt="חשק, חברה של קפה"></a>
    <div class="hdr-end">
      <button class="cart" id="cart" type="button" aria-label="סל קניות"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M5 8h14l-1.2 11.2a1 1 0 0 1-1 .8H7.2a1 1 0 0 1-1-.8L5 8z" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linejoin="round"/><path d="M9 10V7a3 3 0 0 1 6 0v3" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg><span id="count" class="badge">0</span></button>
    </div>
  </div>
  <div id="mnav" hidden><div class="in">{nav}</div></div>
</header>

<main id="top">
{body}
</main>

<footer>
  <div class="in">
    <a class="logo" href="index.html"><img src="img/logo.svg" alt="חשק, חברה של קפה"></a>
    <nav aria-label="תחתון">{fnav}<a href="#">תקנון</a><a href="#">משלוחים והחזרות</a><a href="https://www.instagram.com/heshek.coffee/" target="_blank" rel="noopener">אינסטגרם</a></nav>
    <small><span class="todo">שם החברה, ח.פ. וכתובת</span></small>
  </div>
</footer>

</div>
<script src="site.js"></script>
</body>
</html>
'''
def page(fn,title,desc,body,active=None):
    html=LAYOUT.format(title=title,desc=desc,body=body,nav=nav(active),fnav=nav(None))
    open(os.path.join(R,'..',fn),'w',encoding='utf-8').write(html)

def L(s):  # in-page anchors -> pages
    return (s.replace('href="#shop"','href="shop.html"').replace('href="#how"','href="how.html"')
             .replace('href="#biz"','href="business.html"').replace('href="#story"','href="story.html"'))

hero=L(part('hero'))
shop=part('shop')
cards=re.findall(r'<article class="card.*?</article>',shop,re.S)
# product links
cards[0]=cards[0].replace('<h3>Indonesia</h3>','<h3><a href="product.html">Indonesia</a></h3>')
cats=['drip','drip','drip','drip','ground','soon']
cards_c=[c.replace('<article class="card','<article data-cat="%s" class="card'%k,1) for c,k in zip(cards,cats)]
how=part('how'); where=part('where'); biz=part('biz'); story=part('story'); insta=part('insta')

# ---------- home ----------
home_shop=shop.replace('<div class="grid">','<div class="grid rail">').replace('</div>\n  </div>\n</section>','</div>\n    <p class="more"><a class="btn alt" href="shop.html">לכל המוצרים</a></p>\n  </div>\n</section>')
home_how=how.replace('<p class="note"><span class="todo">כמות מים וזמן חליטה לפי ההמלצה שלך</span></p>','<p class="more"><a class="btn alt" href="how.html">עוד על ההכנה</a></p>')
ticker=re.search(r'<div class="ticker".*?</div></div>',biz,re.S).group(0)
floaty=re.search(r'<div class="ph floaty">.*?</div>',biz,re.S).group(0)
leadform=re.search(r'    <form id="bizform".*?</form>',biz,re.S).group(0)
home_biz=ticker+'''

<section id="biz" class="biz">
  <div class="in">
    <div class="head">
      <h2>הקפה שלכם. המותג שלכם. הביצוע שלנו.</h2>
      <p>דריפ באגז עם השם שלכם. לבתי קפה, לעסקים, ולכל מי שמתכנן אירוע.</p>
    </div>
    <div class="cols">
      <div>'''+floaty+'''</div>
      <div>
        <p class="proof" style="margin-top:0"><span>כבר הכנו</span><b>4,500</b><span>שקיות ממותגות ל־Wix, למטבחונים שלהם.</span></p>
        <div class="event">
          <h3>יש לכם אירוע?</h3>
          <p>חתונה, כנס, יום כיף לעובדים. במקום עוד מגנט שנשאר במגירה, שקית קפה עם השם שלכם שמישהו באמת ישתה מחר בבוקר.</p>
        </div>
        <ul class="fits"><li>בתי קפה</li><li>מטבחונים במשרד</li><li>צימרים</li><li>חתונות</li><li>כנסים</li><li>מתנות לעובדים</li></ul>
        <p class="more"><a class="btn alt" href="business.html">איך זה עובד ומה אפשר</a></p>
      </div>
    </div>
'''+leadform+'''
  </div>
</section>'''
home_story='''<section id="story" class="story">
  <div class="in cols">
    <div class="panel"><span class="todo pin">תמונה: ידיים אורזות, או איור שלך</span><img src="img/hug.jpg" alt="איור: בחורה מחבקת כוס קפה ענקית"></div>
    <div>
      <div class="head" style="margin-bottom:16px"><h2>חברה של קפה</h2></div>
      <div class="prose">
        <p class="big">20 שנה אני בקפה. איפשהו בדרך הלך לי החשק, אז חזרתי לדבר עצמו: הקפה.</p>
        <p>חשק זה גם ראשי תיבות: חברה של קפה. כזה שתמיד בא איתך.</p>
      </div>
      <p class="more"><a class="btn alt" href="story.html">לסיפור המלא</a></p>
    </div>
  </div>
</section>'''
page('index.html','חשק, חברה של קפה','דריפ באגז של חשק. קורעים, תולים, מוזגים.',
     '\n\n'.join([hero,home_shop,home_how,where,home_biz,home_story,insta]))

# ---------- shop ----------
page('shop.html','חנות | חשק','דריפ באגז, קפה ומארזים של חשק.','''<div class="pagehead sun"><div class="in">
  <div class="label">חנות</div>
  <h1>קפה</h1>
  <p>דריפ באגז וקפה טורקי. פולים, כוסות ומארזים יגיעו בהמשך, כל אחד בקטגוריה משלו.</p>
</div></div>
<section><div class="in">
  <div class="chips" role="group" aria-label="סינון">
    <button class="chip" type="button" data-filter="all" aria-pressed="true">הכול</button>
    <button class="chip" type="button" data-filter="drip" aria-pressed="false">דריפ באגז</button>
    <button class="chip" type="button" data-filter="ground" aria-pressed="false">קפה טורקי</button>
    <button class="chip" type="button" data-filter="soon" aria-pressed="false">בקרוב</button>
  </div>
  <div class="grid">
'''+'\n'.join(cards_c)+'''
  </div>
  <p class="more"><span class="todo">עוד מוצרים: קפה של בלומס במשקל, כוסות GONA</span></p>
</div></section>''','shop.html')

# ---------- product ----------
page('product.html','Indonesia | חשק','דריפ באגז Indonesia של חשק.','''<section><div class="in">
  <p class="crumbs"><a href="shop.html">חנות</a> / דריפ באגז / Indonesia</p>
  <div class="product" style="margin-top:16px">
    <div class="gallery">
      <div class="main"><img src="img/products/indonesia.jpg" alt="דריפ באגז Indonesia"></div>
      <img class="thumb" src="img/hang.jpg" alt="השקית תלויה על כוס">
      <img class="thumb" src="img/pour.jpg" alt="מוזגים מים">
      <img class="thumb" src="img/hand-bag.jpg" alt="השקית ביד">
    </div>
    <div class="pinfo">
      <div class="label">דריפ באגז</div>
      <h1>Indonesia</h1>
      <p><span class="todo">שתי שורות על הקפה: מאיפה הוא ואיך הוא בכוס</span></p>
      <dl class="facts">
        <dt>מקור</dt><dd><span class="todo">להשלים</span></dd>
        <dt>קלייה</dt><dd><span class="todo">להשלים</span></dd>
        <dt>בכוס</dt><dd><span class="todo">טעמים</span></dd>
        <dt>בקופסה</dt><dd><span class="todo">כמה שקיות</span></dd>
        <dt>בכל שקית</dt><dd><span class="todo">כמה גרם</span></dd>
      </dl>
      <p class="price" style="font-size:1.8rem">₪ <span class="todo">מחיר</span></p>
      <div class="buy">
        <div class="qty"><button type="button" data-step="1" aria-label="עוד אחד">+</button><input id="qty" value="1" inputmode="numeric" aria-label="כמות"><button type="button" data-step="-1" aria-label="אחד פחות">−</button></div>
        <button class="add" type="button">הוספה לסל</button>
      </div>
      <div class="mini">
        <b>קורעים. תולים. מוזגים.</b>
        <span>צריך רק כוס ומים חמים. <a href="how.html">איך מכינים</a></span>
      </div>
      <p><span class="todo">משלוח: זמנים ועלות</span></p>
    </div>
  </div>
</div></section>''')

# ---------- how ----------
how_page=how.replace('<h2>איך מכינים</h2>','<h2>שלושה צעדים</h2>')
page('how.html','איך מכינים | חשק','איך מכינים דריפ באג: קורעים, תולים, מוזגים.','''<div class="pagehead sky"><div class="in">
  <div class="label">איך מכינים</div>
  <h1>קורעים. תולים. מוזגים.</h1>
  <p>דריפ באג הוא פילטר קטן עם קפה טחון בפנים. תולים אותו על הכוס ומוזגים מים, כמו פילטר רגיל, רק בלי הציוד.</p>
</div></div>
'''+how_page+'''
<section><div class="in">
  <div class="head"><h2>כמה דברים קטנים</h2></div>
  <div class="tips">
    <div class="tip"><h3>כוס רחבה</h3><p>הכנפיים צריכות להיתפס על השפה. כוס רחבה ונמוכה עובדת הכי טוב.</p></div>
    <div class="tip"><h3>לאט</h3><p>מוזגים קצת, מחכים שיירד, וממשיכים. ככה המים עוברים דרך כל הקפה.</p></div>
    <div class="tip"><h3>בלי ציוד</h3><p>קומקום, מיחם או מים חמים ממכונה במשרד. זה מספיק.</p></div>
  </div>
  <p class="more"><span class="todo">כמות מים וזמן חליטה מדויקים לפי ההמלצה שלך</span></p>
</div></section>
<section><div class="in">
  <div class="head"><h2>שאלות</h2></div>
  <div class="faq">
    <details><summary>כמה זמן הקפה נשאר טרי?</summary><p><span class="todo">תשובה ממך</span></p></details>
    <details><summary>אפשר להכין עם חלב?</summary><p><span class="todo">תשובה ממך</span></p></details>
    <details><summary>מה עושים עם השקית אחרי?</summary><p><span class="todo">תשובה ממך</span></p></details>
  </div>
</div></section>''','how.html')

# ---------- business ----------
page('business.html','לעסקים | חשק','דריפ באגז ממותגים לבתי קפה, בתי קלייה ועסקים.',biz,'business.html')

# ---------- story ----------
page('story.html','הסיפור | חשק','למה חשק, ומי מאחוריו.','''<div class="pagehead blush"><div class="in">
  <div class="label">הסיפור</div>
  <h1>חברה של קפה</h1>
</div></div>
'''+story.replace('<div class="head" style="margin-bottom:16px"><h2>חברה של קפה</h2></div>','')+'\n'+where,'story.html')
page('contact.html','צרו קשר | חשק','איך מגיעים לחשק.','''<div class="pagehead"><div class="in">
  <div class="label">צרו קשר</div>
  <h1>מדברים?</h1>
  <p>שאלה על הזמנה, רעיון לשיתוף פעולה, או סתם בא לכם לדבר על קפה.</p>
</div></div>
<section><div class="in contact">
  <div class="ways">
    <div class="way"><span class="label">וואטסאפ</span><b><span class="todo">מספר</span></b></div>
    <div class="way"><span class="label">מייל</span><b><span class="todo">כתובת מייל</span></b></div>
    <div class="way"><span class="label">אינסטגרם</span><b><a href="https://www.instagram.com/heshek.coffee/" target="_blank" rel="noopener" dir="ltr">@heshek.coffee</a></b></div>
    <div class="way"><span class="label">לעסקים ואירועים</span><b><a href="business.html">לטופס ההזמנה</a></b></div>
  </div>
  <form id="bizform" class="leadform" novalidate>
    <h3>השאירו הודעה</h3>
    <div class="f2">
      <label for="c-name">שם<input id="c-name" name="name" autocomplete="name"></label>
      <label for="c-phone">טלפון או מייל<input id="c-phone" name="contact" autocomplete="email" dir="ltr"></label>
    </div>
    <label for="c-msg">ההודעה<textarea id="c-msg" name="msg"></textarea></label>
    <button class="btn" type="submit">שליחה</button>
    <p id="formmsg" aria-live="polite"></p>
  </form>
</div></section>''','contact.html')
print('built')
