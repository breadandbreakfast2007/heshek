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
(function(){
  var img=document.getElementById('cupImg');if(!img)return;
  var P={bino:{name:'Bino',vol:'230 מ״ל',cup:109,sleeve:60},camino:{name:'Camino',vol:'340 מ״ל',cup:129,sleeve:60}};
  var size='bino',color='oat';
  var $=function(id){return document.getElementById(id);};
  function render(){
    var p=P[size];
    img.src='img/cups/'+size+'-'+color+'.webp';
    img.alt='כוס Fressko '+p.name+' בצבע '+$('colorName').textContent;
    $('cupName').textContent=p.name;$('cupSub').textContent=p.vol+' · ציפוי קרמי פנימי';$('factVol').textContent=p.vol;
    $('sleevePrice').textContent=p.sleeve;
    $('cupTotal').textContent=p.cup+($('sleeve').checked?p.sleeve:0);
  }
  document.querySelectorAll('input[name=cupsize]').forEach(function(r){r.addEventListener('change',function(){size=r.value;render();});});
  document.querySelectorAll('.swatches button').forEach(function(b){b.addEventListener('click',function(){
    document.querySelectorAll('.swatches button').forEach(function(x){x.setAttribute('aria-checked',String(x===b));});
    color=b.getAttribute('data-color');$('colorName').textContent=b.getAttribute('data-name');render();
  });});
  $('sleeve').addEventListener('change',render);
  function fromHash(){var h=location.hash.replace('#','');if(P[h]){size=h;var r=document.querySelector('input[name=cupsize][value='+h+']');if(r)r.checked=true;render();
    var c=document.getElementById('cup');if(c)setTimeout(function(){c.scrollIntoView({block:'start'});},30);}}
  window.addEventListener('hashchange',fromHash);fromHash();render();
})();
(function(){
  var v=document.querySelector('.vidhero.light video'),c=document.querySelector('.vcap');if(!v||!c)return;
  var s=c.querySelector('span'),cur='';
  var C=[[3.0,4.8,'זוכת פרסים · עוצבה באוסטרליה'],[6.3,8.4,'שומרת חום יותר מ־3 שעות'],[8.8,10.6,'לא נוזלת. בכלל.'],[12.5,14.2,'פשוט כוס הקפה הרב־פעמית הכי טובה בעולם']];
  v.addEventListener('timeupdate',function(){var t=v.currentTime,txt='';for(var i=0;i<C.length;i++)if(t>=C[i][0]&&t<C[i][1])txt=C[i][2];
    if(txt!==cur){cur=txt;if(txt){s.textContent=txt;c.classList.add('on')}else c.classList.remove('on')}});
})();
