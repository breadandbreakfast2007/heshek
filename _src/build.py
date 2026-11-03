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
    <small>ברד אנד ברקפסט בע״מ · ח.פ. 513969154 · ז׳בוטינסקי 3, רעננה</small>
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
cats=['drip']*7+['ground','soon']
cards_c=[c.replace('<article class="card','<article data-cat="%s" class="card'%k,1) for c,k in zip(cards,cats)]
how=part('how'); where=part('where'); biz=part('biz'); story=part('story'); insta=part('insta')

# ---------- home ----------
home_shop=shop.replace('<div class="grid">','<div class="grid rail">').replace('</div>\n  </div>\n</section>','</div>\n    <p class="more"><a class="btn alt" href="shop.html">לכל המוצרים</a></p>\n  </div>\n</section>')
home_how=how.replace('<p class="note">בכל שקית 12 גרם קפה.</p>','<p class="more"><a class="btn alt" href="how.html">עוד על ההכנה</a></p>')
ticker=re.search(r'<div class="ticker".*?</div></div>',biz,re.S).group(0)
floaty=re.search(r'<div class="ph floaty">.*?</div>',biz,re.S).group(0)
leadform=re.search(r'    <form id="bizform".*?</form>',biz,re.S).group(0)
home_biz=ticker+'''

<section id="biz" class="biz">
  <div class="in">
    <div class="head">
      <h2>דריפ באגז עם המותג שלכם</h2>
      <p>לחברות, לאירועים ולמתנות, עם הקפה שלנו. ולבתי קלייה ובתי קפה, עם הקפה שלהם.</p>
    </div>
    <div class="cols">
      <div>'''+floaty+'''</div>
      <div>
        <div class="proof"><p><b>Wix</b> הזמינו 4,500 שקיות חשק עם הלוגו שלהם. 1,500 חולקו לעובדים ביום הקפה הבינלאומי, ו־3,000 נמכרות בדלי שלהם.</p><p>וב<b>יקב רמות נפתלי</b> מוכרים למבקרים שקיות עם המותג של היקב, בסוף סיור היין.</p></div>
        <div class="works" aria-label="עבודות שעשינו"><figure><img src="img/works/wix-cafe.jpg" alt="דריפ באג ממותג WIX CAFE" loading="lazy"><figcaption>Wix</figcaption></figure><figure><img src="img/works/ramot-naftaly.jpg" alt="דריפ באג ממותג של יקב רמות נפתלי" loading="lazy"><figcaption>יקב רמות נפתלי</figcaption></figure></div>
        <div class="event">
          <h3>יש לכם אירוע?</h3>
          <p>חתונה, כנס או מתנה לעובדים. דריפ באגז עם העיצוב שלכם.</p>
        </div>
        <p class="fits-label">מתאים ל:</p>
        <ul class="fits"><li>בתי קפה</li><li>בתי קלייה</li><li>מטבחונים במשרד</li><li>צימרים</li><li>חתונות</li><li>כנסים</li><li>מתנות לעובדים</li></ul>
        <p class="more"><a class="btn alt" href="business.html">לפרטים והצעת מחיר</a></p>
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
        <p class="big">חשק נולד מתוך ברד אנד ברקפסט, כדי לתת לקפה שם משלו ולקחת אותו גם מעבר לבית הקפה.</p>
        <p>קפה מבתי קלייה בארץ, בדריפ באג אישי שקל להכין איפה שבא לכם.</p>
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
  <p>דריפ באגז וקפה טורקי.</p>
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
</div></section>''','shop.html')

# ---------- product ----------
page('product.html','אינדונזיה | חשק','דריפ באגז אינדונזיה של חשק.','''<section><div class="in">
  <p class="crumbs"><a href="shop.html">חנות</a> / דריפ באגז / אינדונזיה</p>
  <div class="product" style="margin-top:16px">
    <div class="gallery">
      <div class="main"><img src="img/products/indonesia.jpg" alt="דריפ באגז אינדונזיה"></div>
      <img class="thumb" src="img/hang.jpg" alt="השקית תלויה על כוס">
      <img class="thumb" src="img/pour.jpg" alt="מוזגים מים">
      <img class="thumb" src="img/hand-bag.jpg" alt="השקית ביד">
    </div>
    <div class="pinfo">
      <div class="label">דריפ באגז</div>
      <h1>אינדונזיה</h1>
      <p class="sub" dir="ltr">Sumatra · Sesongot · Gayo · Natural</p>
      <p>מאינדונזיה לרעננה. מכאן לאן שבא לכם.</p>
      <p>ענבים אדומים, דומדמניות ושוקולד חלב. מתוק ונקי, בלי הכבדות הרגילה של סומטרה.</p>
      <dl class="facts">
        <dt>מקור</dt><dd>גאיו, סומטרה, אינדונזיה</dd>
        <dt>גובה</dt><dd>1,300–1,600 מ׳</dd>
        <dt>עיבוד</dt><dd dir="ltr">Natural</dd>
        <dt>קלייה</dt><dd>בלומס, פרדס חנה · בינונית־בהירה</dd>
        <dt>בכוס</dt><dd>ענבים אדומים, דומדמניות, שוקולד חלב</dd>
        <dt>בקופסה</dt><dd>10 שקיות</dd>
        <dt>בכל שקית</dt><dd>12 גרם</dd>
      </dl>
      <fieldset class="opts"><legend class="sr-only">גודל</legend>
        <label><input type="radio" name="size" value="box" checked> קופסה של 10 · ₪75</label>
        <label><input type="radio" name="size" value="one"> שקית בודדת · ₪10</label>
      </fieldset>
      <div class="buy">
        <div class="qty"><button type="button" data-step="1" aria-label="עוד אחד">+</button><input id="qty" value="1" inputmode="numeric" aria-label="כמות"><button type="button" data-step="-1" aria-label="אחד פחות">−</button></div>
        <button class="add" type="button">הוספה לסל</button>
      </div>
      <div class="mini">
        <b>קורעים. תולים. מוזגים.</b>
        <span>בלי ציוד מיוחד, בלי התעסקות. <a href="how.html">איך מכינים</a></span>
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
  <p>דריפ באג הוא פילטר אישי עם קפה טחון. פותחים, תולים על הכוס ומוזגים מים חמים.</p>
</div></div>
'''+how_page+'''
<section><div class="in">
  <div class="head"><h2>כמה דברים קטנים</h2></div>
  <div class="tips">
    <div class="tip"><h3>הכוס</h3><p>בוחרים כוס שהכנפיים נתפסות יציב על השפה שלה, ושגבוהה מספיק כדי שהפילטר לא ישקע בקפה.</p></div>
    <div class="tip"><h3>30 שניות בהתחלה</h3><p>המזיגה הראשונה רק מרטיבה את הקפה. מחכים בערך 30 שניות, והקפה מוכן לשאר המים. קוראים לזה בלום.</p></div>
    <div class="tip"><h3>בלי ציוד מיוחד</h3><p>קומקום, מיחם או מים חמים ממכונה במשרד. זה מספיק.</p></div>
  </div>
</div></section>
<section><div class="in">
  <div class="head"><h2>שאלות</h2></div>
  <div class="faq">
    <details><summary>אפשר להוסיף חלב?</summary><p><span class="todo">תשובה ממך</span></p></details>
  </div>
</div></section>''','how.html')

# ---------- business ----------
page('business.html','לעסקים ואירועים | חשק','דריפ באגז עם המותג שלכם: לחברות, לאירועים, לבתי קלייה ולבתי קפה.',biz,'business.html')

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
    <div class="way"><span class="label">מייל</span><b><a href="mailto:info@heshek.coffee" dir="ltr">info@heshek.coffee</a></b></div>
    <div class="way"><span class="label">אינסטגרם</span><b><a href="https://www.instagram.com/heshek.coffee/" target="_blank" rel="noopener" dir="ltr">@heshek.coffee</a></b></div>
    <div class="way"><span class="label">לעסקים ואירועים</span><b><a href="business.html">לבקשת הצעת מחיר</a></b></div>
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

# ---------- subscription (DRAFT, not in nav) ----------
page('subscription.html','מנוי | חשק','מנוי הדריפ באגז של חשק.','''<div class="pagehead"><div class="in">
  <div class="label">מנוי הדריפ באגז של חשק</div>
  <h1>חשק קבוע.</h1>
  <p>יש קפה שטועמים ורוצים שוב.<br>ויש את זה שעוד לא מכירים.</p>
  <p>בכל חודש נשלח לכם מארז דריפ באגז עם קפה ששווה לפנות בשבילו כמה דקות. אפשר להישאר עם האהוב עליכם, לטעום כמה סוגים או להשאיר לנו את הבחירה.</p>
  <p><a class="btn" href="#plans">מה במנוי?</a></p>
</div></div>
<section class="tight"><div class="in">
  <div class="roasters">
    <p class="big">בתי קלייה בארץ עושים דברים נהדרים.</p>
    <p>אנחנו טועמים ובוחרים, ואתם יכולים להכיר את הקפה שלהם כוס בכל פעם.</p>
    <p class="nos">בלי להתחייב לשקית פולים שלמה, בלי מטחנה ובלי ציוד מיוחד.</p>
  </div>
</div></section>
<section id="plans"><div class="in">
  <div class="head"><h2>מכירים את הטעם שלכם, או שבא לכם לגלות?</h2></div>
  <fieldset class="plans"><legend class="sr-only">מסלול</legend>
    <label class="plan"><input type="radio" name="plan" value="one" checked>
      <h3>מצאנו אחד.</h3><span class="kind">קפה קבוע</span>
      <p>הקפה שאהבתם, שוב אצלכם. 10 דריפ באגז מאותו סוג בכל חודש, לרגעים שבהם אתם יודעים בדיוק מה בא לכם.</p></label>
    <label class="plan"><input type="radio" name="plan" value="mix">
      <h3>עוד לא החלטנו.</h3><span class="kind">מארז מגוון</span>
      <p>חמישה סוגי קפה, שתי שקיות מכל אחד. לטעום זה לצד זה, לחזור לעוד כוס ולגלות מה הכי אהבתם.</p></label>
    <label class="plan"><input type="radio" name="plan" value="pick">
      <h3>תבחרו לנו.</h3><span class="kind">בחירה חודשית שלנו</span>
      <p>בכל חודש נבחר בשבילכם קפה אחר. אתם תגלו מה הגיע כשתפתחו את החבילה.</p></label>
  </fieldset>
</div></section>
<section><div class="in">
  <div class="pinfo" style="max-width:560px">
    <h2>כמה מארזים בחודש</h2>
    <fieldset class="opts"><legend class="sr-only">כמה מארזים בחודש</legend>
      <label><input type="radio" name="boxes" value="1" checked> 1</label>
      <label><input type="radio" name="boxes" value="2"> 2</label>
      <label><input type="radio" name="boxes" value="3"> 3</label>
    </fieldset>
    <dl class="facts">
      <dt>בכל מארז</dt><dd>10 דריפ באגז, 12 גרם בכל אחד</dd>
      <dt>מחיר</dt><dd><span class="todo">מחיר למארז במנוי</span></dd>
      <dt>משלוח</dt><dd><span class="todo">ימים ועלות</span></dd>
      <dt>עצירה וביטול</dt><dd><span class="todo">תנאים</span></dd>
    </dl>
    <div class="buy"><button class="add" type="button">זה המנוי שלי</button></div>
  </div>
</div></section>''')
