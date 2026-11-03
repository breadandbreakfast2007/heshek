(function(){
  var btn=document.getElementById('menuBtn'),nav=document.getElementById('mnav');
  if(btn&&nav){
    btn.addEventListener('click',function(){var open=nav.hidden;nav.hidden=!open;btn.setAttribute('aria-expanded',String(open));});
  }
  var n=0,count=document.getElementById('count');if(count)count.setAttribute('data-zero','');
  document.querySelectorAll('.add').forEach(function(b){b.addEventListener('click',function(){
    if(b.hasAttribute('data-soon')){b.textContent='נעדכן אותך';b.disabled=true;return;}
    n+=parseInt((document.getElementById('qty')||{}).value||1,10)||1;if(count){count.textContent=n;count.removeAttribute('data-zero');}
    var t=b.textContent;b.textContent='נוסף ✓';setTimeout(function(){b.textContent=t;},1200);
  });});
  var f=document.getElementById('bizform');
  if(f)f.addEventListener('submit',function(e){
    e.preventDefault();document.getElementById('formmsg').textContent='זו גרסת בדיקה. הטופס עוד לא שולח.';
  });
  document.querySelectorAll('[data-filter]').forEach(function(c){c.addEventListener('click',function(){
    var v=c.getAttribute('data-filter');
    document.querySelectorAll('[data-filter]').forEach(function(x){x.setAttribute('aria-pressed',String(x===c));});
    document.querySelectorAll('[data-cat]').forEach(function(card){card.hidden=!(v==='all'||card.getAttribute('data-cat')===v);});
  });});
  var q=document.getElementById('qty');
  document.querySelectorAll('[data-step]').forEach(function(b){b.addEventListener('click',function(){
    q.value=Math.max(1,(parseInt(q.value,10)||1)+parseInt(b.getAttribute('data-step'),10));
  });});
})();
(function(){
  if(!('IntersectionObserver' in window))return;
  var els=document.querySelectorAll('section .prose, section blockquote');
  document.documentElement.classList.add('js');
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});
  els.forEach(function(el){el.classList.add('reveal');io.observe(el);});
})();
