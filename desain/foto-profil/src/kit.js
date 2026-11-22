// Kit gambar akun Rahasia Kursi Dokter Gigi: palet, cengkeh, gigi, tetes, panah, tangan, map.
const C={krem:'#FFF7EF',map:'#F6E3CC',or:'#FA7209',ortua:'#CF6515',gelap:'#2A2A2A',coklat:'#7A3608',amber:'#F8C000',glove:'#F7F3EE'};
const clove=(x,y,s)=>`<g transform="translate(${x},${y}) scale(${s})"><path d="M-14 0 L14 0 L6 230 Q0 244 -6 230 Z" fill="${C.coklat}"/><g fill="${C.coklat}"><path d="M0 4 Q-46 -10 -58 -52 Q-22 -46 0 -14Z"/><path d="M0 4 Q46 -10 58 -52 Q22 -46 0 -14Z"/><path d="M-8 0 Q-30 -40 -14 -70 Q2 -40 8 0Z"/><path d="M8 0 Q30 -40 14 -70 Q-2 -40 -8 0Z"/></g><circle cy="-62" r="34" fill="${C.coklat}"/><circle cx="-10" cy="-72" r="10" fill="#fff" opacity=".18"/></g>`;
const wisp=(x,y,o)=>`<path d="M${x} ${y} q-36 -45 0 -90 q36 -45 0 -90" fill="none" stroke="${C.ortua}" stroke-width="12" stroke-linecap="round" opacity="${o}"/>`;
const toothPath="M-60 -70 C-110 -70 -110 10 -80 40 C-65 60 -70 120 -45 125 C-20 130 -20 50 0 50 C20 50 20 130 45 125 C70 120 65 60 80 40 C110 10 110 -70 60 -70 C30 -70 20 -55 0 -55 C-20 -55 -30 -70 -60 -70Z";
const tooth=(x,y,s,extra='')=>`<g transform="translate(${x},${y}) scale(${s})"><path d="${toothPath}" fill="#fff" stroke="${C.gelap}" stroke-width="8" stroke-linejoin="round"/>${extra}</g>`;
const drop=(x,y,s)=>`<g transform="translate(${x},${y}) scale(${s})"><path d="M0 -70 C30 -25 46 0 46 26 A46 46 0 0 1 -46 26 C-46 0 -30 -25 0 -70Z" fill="${C.amber}" stroke="${C.gelap}" stroke-width="7"/><path d="M-20 18 q0 22 18 30" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".7"/></g>`;
const arrow=(x1,y,x2)=>`<path d="M${x1} ${y} C${(x1+x2)/2} ${y-28} ${(x1+x2)/2} ${y+18} ${x2} ${y}" fill="none" stroke="${C.gelap}" stroke-width="9" stroke-linecap="round"/><path d="M${x2-24} ${y-20} L${x2+2} ${y} L${x2-22} ${y+22}" fill="none" stroke="${C.gelap}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>`;
// tangan bersarung tangan (varian 1, tanpa wajah)
const stampHand=(x,y,s)=>`<g transform="translate(${x},${y}) scale(${s})">
 <path d="M30 -150 L170 -330 L250 -270 L105 -95 Z" fill="${C.glove}" stroke="${C.gelap}" stroke-width="8" stroke-linejoin="round"/>
 <path d="M160 -318 L240 -258" stroke="${C.ortua}" stroke-width="24"/>
 <rect x="-110" y="60" width="220" height="50" rx="10" fill="${C.gelap}"/>
 <rect x="-90" y="22" width="180" height="44" rx="10" fill="${C.coklat}"/>
 <rect x="-26" y="-70" width="52" height="96" rx="14" fill="${C.coklat}"/>
 <circle cy="-100" r="46" fill="${C.coklat}"/>
 <ellipse cx="0" cy="-128" rx="86" ry="60" fill="${C.glove}" stroke="${C.gelap}" stroke-width="8"/>
 ${[-68,-32,4,40].map(fx=>`<rect x="${fx}" y="-104" width="34" height="62" rx="17" fill="${C.glove}" stroke="${C.gelap}" stroke-width="7"/>`).join('')}
 <path d="M-80 -150 C-120 -130 -118 -86 -86 -76" fill="${C.glove}" stroke="${C.gelap}" stroke-width="7" stroke-linecap="round"/></g>`;
const pointHand=(x,y,s)=>`<g transform="translate(${x},${y}) scale(${s})">
 <rect x="-270" y="-62" width="120" height="124" rx="10" fill="${C.glove}" stroke="${C.gelap}" stroke-width="8"/>
 <rect x="-262" y="-62" width="34" height="124" fill="${C.ortua}"/>
 <rect x="-165" y="-70" width="190" height="140" rx="46" fill="${C.glove}" stroke="${C.gelap}" stroke-width="8"/>
 <rect x="-10" y="-70" width="190" height="46" rx="23" fill="${C.glove}" stroke="${C.gelap}" stroke-width="8"/>
 ${[-18,14,46].map(fy=>`<rect x="-20" y="${fy}" width="72" height="34" rx="17" fill="${C.glove}" stroke="${C.gelap}" stroke-width="7"/>`).join('')}
 <rect x="-100" y="-104" width="110" height="44" rx="22" fill="${C.glove}" stroke="${C.gelap}" stroke-width="8" transform="rotate(-8 -45 -82)"/></g>`;
const logo=`<img class="logo" src="logo-upg-transparan.png">`;
const folderBlock=(tab,top=470,h=820)=>`<div class="tab" style="left:76px;top:${top-50}px">${tab}</div><div class="folder" style="left:80px;right:140px;top:${top+10}px;height:${h}px"></div>`;
const sub=t=>`<div class="sub">${t}</div>`;
