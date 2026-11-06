export const TIMING = Object.freeze({departure:2.4,flight:1.45,arrival:2.4,fade:.45,cycle:6.7});
export const clamp = (x,a=0,b=1)=>Math.max(a,Math.min(b,x));
export const ease = x => (x=clamp(x))<.5 ? 4*x*x*x : 1-Math.pow(-2*x+2,3)/2;
export function unit(lat,lon){const a=lat*Math.PI/180,b=lon*Math.PI/180;return [Math.cos(a)*Math.sin(b),Math.sin(a),Math.cos(a)*Math.cos(b)];}
export function arc(a,b,t,lift=true){
 const dot=clamp(a.reduce((v,x,i)=>v+x*b[i],0),-1,1),angle=Math.acos(dot);
 let tangent=b.map((x,i)=>x-dot*a[i]);let len=Math.hypot(...tangent);
 if(len<1e-8){const axis=Math.abs(a[0])<.8?[1,0,0]:[0,1,0];const d=axis.reduce((s,x,i)=>s+x*a[i],0);tangent=axis.map((x,i)=>x-d*a[i]);len=Math.hypot(...tangent);}
 const r=lift?1.006+Math.sin(Math.PI*t)*(.03+.13*angle):1;
 return a.map((x,i)=>(x*Math.cos(angle*t)+tangent[i]/len*Math.sin(angle*t))*r);
}
export function spring(s,target,dt,rate=7.5){const d=s.x-target,e=Math.exp(-rate*dt),j=(s.v+rate*d)*dt;s.x=target+(d+j)*e;s.v=(s.v-rate*j)*e;}
export function phase(t){return t<TIMING.departure?'Departure ripple':t<TIMING.departure+TIMING.flight?'In flight':t<TIMING.cycle-TIMING.fade?'Arrival ripple':'Transition';}
