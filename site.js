(function(){
  var btn=document.getElementById('menuBtn'),nav=document.getElementById('mnav');
  if(btn&&nav){
    btn.addEventListener('click',function(){var open=nav.hidden;nav.hidden=!open;btn.setAttribute('aria-expanded',String(open));});
  }
  var n=0,count=document.getElementById('count');
  document.querySelectorAll('.add').forEach(function(b){b.addEventListener('click',function(){
    if(b.hasAttribute('data-soon')){b.textContent='נעדכן אותך';b.disabled=true;return;}
    n+=parseInt((document.getElementById('qty')||{}).value||1,10)||1;if(count)count.textContent=n;
    var t=b.textContent;b.textContent='נוסף ✓';setTimeout(function(){b.textContent=t;},1200);
  });});
  var f=document.getElementById('bizform');
  if(f)f.addEventListener('submit',function(e){
    e.preventDefault();document.getElementById('formmsg').textContent='זו טיוטה, הטופס עוד לא שולח. באתר האמיתי הפנייה תגיע אליך למייל.';
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
