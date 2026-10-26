"""Générateur de visuels Facebook SANIPURE (style worker, 1440x1800).
Gabarits : photo(), yellow_list(), offer(), myth(). Les fichiers sortent dans out/."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F=ROOT+'/fonts/'
def M(w,s,it=False): return ImageFont.truetype(f'{F}montserrat-{w}-{"italic" if it else "normal"}.ttf',s)
W,H=1440,1800
Y=(255,174,0); K=(12,12,12); WH=(255,255,255); G=(190,190,190)
U=ROOT+'/photos/'
OUT=ROOT+'/out/'; os.makedirs(OUT,exist_ok=True)
LOGO=Image.open(ROOT+'/tools/logo-sanipure.png').convert('RGBA')

def tr(d,xy,t,f,fill,track=0,anchor='l'):
    x,y=xy; ws=[d.textlength(c,font=f) for c in t]; tot=sum(ws)+track*(len(t)-1)
    if anchor=='r': x-=tot
    for c,w in zip(t,ws): d.text((x,y),c,font=f,fill=fill); x+=w+track
    return tot

def cover(src,focus,size):
    im=Image.open(src).convert('RGB'); tw,th=size; r=max(tw/im.width,th/im.height)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    l=int(min(max(focus[0]*im.width-tw/2,0),im.width-tw)); t=int(min(max(focus[1]*im.height-th/2,0),im.height-th))
    im=im.crop((l,t,l+tw,t+th))
    im=ImageEnhance.Contrast(im).enhance(1.08); im=ImageEnhance.Color(im).enhance(0.95)
    return im

def logo(im,x,y,w):
    l=LOGO.resize((w,round(LOGO.height*w/LOGO.width)),Image.LANCZOS); im.alpha_composite(l,(x,y)); return l.height

def stripes(im,y,h=26):
    s=Image.new('RGBA',(W,h),Y+(255,)); d=ImageDraw.Draw(s)
    for x in range(-h,W+h,56): d.polygon([(x,h),(x+28,h),(x+28+h,0),(x+h,0)],fill=K)
    im.alpha_composite(s,(0,y))

def wrap(d,text,f,maxw):
    out=[]
    for para in text.split('\n'):
        line=''
        for w in para.split():
            t=(line+' '+w).strip()
            if d.textlength(t,font=f)<=maxw: line=t
            else: out.append(line); line=w
        out.append(line)
    return out

def tag(d,x,y,text,bg=Y,fg=K,size=24):
    f=M(800,size); tw=tr(ImageDraw.Draw(Image.new('RGB',(1,1))),(0,0),text,f,fg,track=4)
    d.rectangle((x,y,x+tw+44,y+size+30),fill=bg); tr(d,(x+22,y+14),text,f,fg,track=4)
    return size+30

def headline(d,x,y,parts,size,maxw,col=WH,hi=Y):
    # parts: list of lines, each line list of (text, highlight)
    while max(sum(d.textlength(t+' ',font=M(900,size)) for t,_ in l)-d.textlength(' ',font=M(900,size)) for l in parts)>maxw: size-=2
    f=M(900,size); lh=int(size*1.02)
    for line in parts:
        cx=x
        for txt,h in line:
            d.text((cx,y),txt,font=f,fill=hi if h else col); cx+=d.textlength(txt+' ',font=f)
        y+=lh
    return y

def footer(im,d,left,right,dark=True):
    col=WH if dark else K
    tr(d,(96,H-118),left,M(700,22),col,track=4)
    tr(d,(W-96,H-118),right,M(700,22),Y if dark else K,track=4,anchor='r')
    stripes(im,H-26)

def photo(name,src,focus,eyebrow,lines,sub,num,cta,ph_h=1060):
    im=Image.new('RGBA',(W,H),K+(255,))
    im.alpha_composite(cover(src,focus,(W,ph_h)).convert('RGBA'),(0,0))
    g=Image.new('RGBA',(W,ph_h),(0,0,0,0)); gd=ImageDraw.Draw(g)
    for y in range(ph_h):
        a=0
        if y<220: a=int(140*(1-y/220)**1.5)
        if y>ph_h-220: a=max(a,int(255*((y-(ph_h-220))/220)**1.6))
        gd.line((0,y,W,y),fill=K+(a,))
    im.alpha_composite(g)
    logo(im,72,64,360)
    d=ImageDraw.Draw(im)
    tr(d,(W-96,84),num,M(800,26),WH,track=3,anchor='r')
    y=ph_h-70; tag(d,96,y,eyebrow)
    y+=110; y=headline(d,92,y,lines,118,W-192)
    y+=28
    for l in wrap(d,sub,M(500,34),W-192): d.text((96,y),l,font=M(500,34),fill=G); y+=48
    footer(im,d,'SANIPURE.FR',cta)
    im.convert('RGB').save(OUT+name,quality=94)

def yellow_list(name,eyebrow,lines,items,note,num,cta):
    im=Image.new('RGBA',(W,H),Y+(255,)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,170),fill=K); logo(im,72,40,360); d=ImageDraw.Draw(im)
    tr(d,(W-96,72),num,M(800,26),WH,track=3,anchor='r')
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d2=ImageDraw.Draw(L)
    y=0; tag(d2,96,y,eyebrow,bg=K,fg=Y)
    y+=110; y=headline(d2,92,y,lines,112,W-192,col=K,hi=WH)
    y+=50
    for i,t in enumerate(items):
        d2.rectangle((96,y,96+110,y+110),fill=K)
        nf=M(900,56); n=f'{i+1}'; d2.text((96+55-d2.textlength(n,font=nf)/2,y+20),n,font=nf,fill=Y)
        ls=wrap(d2,t.upper(),M(800,38),W-96-260)
        ty=y+55-len(ls)*24
        for j,l in enumerate(ls): d2.text((250,ty+j*48),l,font=M(800,38),fill=K)
        y+=146
    y+=30
    for l in wrap(d2,note,M(600,34),W-192): d2.text((96,y),l,font=M(600,34),fill=K); y+=48
    bb=L.getbbox(); h=bb[3]
    top=170+max(60,(H-340-h)//2)
    im.alpha_composite(L.crop((0,0,W,h)),(0,top))
    d=ImageDraw.Draw(im)
    d.rectangle((0,H-170,W,H),fill=K)
    footer(im,d,'SANIPURE.FR',cta)
    im.convert('RGB').save(OUT+name,quality=94)

def offer(name,src,focus,eyebrow,lines,points,cta_btn,num,cta):
    im=Image.new('RGBA',(W,H),K+(255,))
    ph_h=900
    im.alpha_composite(cover(src,focus,(W,ph_h)).convert('RGBA'),(0,0))
    g=Image.new('RGBA',(W,ph_h),(0,0,0,0)); gd=ImageDraw.Draw(g)
    for y in range(220): gd.line((0,y,W,y),fill=K+(int(140*(1-y/220)**1.5),))
    im.alpha_composite(g)
    d=ImageDraw.Draw(im); d.rectangle((0,ph_h,W,H),fill=Y)
    logo(im,72,64,360); d=ImageDraw.Draw(im)
    tr(d,(W-96,84),num,M(800,26),WH,track=3,anchor='r')
    y=ph_h-36; tag(d,96,y,eyebrow,bg=K,fg=Y)
    y+=118; y=headline(d,92,y,lines,108,W-192,col=K,hi=WH)
    y+=24
    x=96
    for p in points:
        f=M(800,28); tw=tr(ImageDraw.Draw(Image.new('RGB',(1,1))),(0,0),p,f,K,track=3)
        d.rectangle((x,y,x+tw+40,y+58),outline=K,width=3); tr(d,(x+20,y+14),p,f,K,track=3); x+=tw+60
    y+=100
    f=M(900,30); tw=tr(ImageDraw.Draw(Image.new('RGB',(1,1))),(0,0),cta_btn,f,WH,track=4)
    d.rectangle((96,y,96+tw+80,y+86),fill=K); tr(d,(136,y+26),cta_btn,f,Y,track=4)
    d.rectangle((0,H-170,W,H),fill=K)
    footer(im,d,'SANIPURE.FR',cta)
    im.convert('RGB').save(OUT+name,quality=94)

def myth(name,eyebrow,claim,verdict,expl,num,cta):
    im=Image.new('RGBA',(W,H),Y+(255,)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,170),fill=K); logo(im,72,40,360); d=ImageDraw.Draw(im)
    tr(d,(W-96,72),num,M(800,26),WH,track=3,anchor='r')
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d2=ImageDraw.Draw(L)
    y=0; tag(d2,96,y,eyebrow,bg=K,fg=Y)
    y+=120; f=M(700,64,True)
    for l in wrap(d2,'« '+claim+' »',f,W-192): d2.text((96,y),l,font=f,fill=K); y+=82
    y+=10; d2.text((80,y),verdict,font=M(900,330),fill=K); y+=400
    d2.rectangle((96,y,96+120,y+8),fill=K); y+=50
    for l in wrap(d2,expl,M(600,40),W-192): d2.text((96,y),l,font=M(600,40),fill=K); y+=56
    h=L.getbbox()[3]; top=170+max(60,(H-340-h)//2)
    im.alpha_composite(L.crop((0,0,W,h)),(0,top)); d=ImageDraw.Draw(im)
    d.rectangle((0,H-170,W,H),fill=K)
    footer(im,d,'SANIPURE.FR',cta)
    im.convert('RGB').save(OUT+name,quality=94)

def fact(name,eyebrow,lines,expl,num,cta,src=None,focus=(0.5,0.5)):
    """Format court du matin (« Le saviez-vous ? »). Avec photo : photo en haut + texte calé en bas.
    Sans photo : fond noir, grand titre centré."""
    x0=96 if src else 150
    L=Image.new('RGBA',(W,H),(0,0,0,0)); d2=ImageDraw.Draw(L)
    y=0; tag(d2,x0,y,eyebrow)
    y+=110; y=headline(d2,x0-4,y,lines,112 if src else 128,W-x0-96)
    y+=34
    for l in wrap(d2,expl,M(500,36),W-x0-96): d2.text((x0,y),l,font=M(500,36),fill=G); y+=52
    h=L.getbbox()[3]
    im=Image.new('RGBA',(W,H),K+(255,))
    if src:
        top=H-200-h; ph_h=min(top+90,1200)
        im.alpha_composite(cover(src,focus,(W,ph_h)).convert('RGBA'),(0,0))
        g=Image.new('RGBA',(W,ph_h),(0,0,0,0)); gd=ImageDraw.Draw(g)
        for yy in range(ph_h):
            a=0
            if yy<220: a=int(140*(1-yy/220)**1.5)
            if yy>ph_h-260: a=max(a,int(255*((yy-(ph_h-260))/260)**1.6))
            gd.line((0,yy,W,yy),fill=K+(a,))
        im.alpha_composite(g)
        logo(im,72,64,360)
    else:
        top=170+max(80,(H-340-h)//2)
        d=ImageDraw.Draw(im); d.rectangle((0,0,W,170),fill=K); logo(im,72,40,360)
        d=ImageDraw.Draw(im); d.rectangle((96,top-20,96+12,top+h+20),fill=Y)
    d=ImageDraw.Draw(im)
    tr(d,(W-96,84 if src else 72),num,M(800,26),WH,track=3,anchor='r')
    im.alpha_composite(L.crop((0,0,W,h)),(0,top)); d=ImageDraw.Draw(im)
    footer(im,d,'SANIPURE.FR',cta)
    im.convert('RGB').save(OUT+name,quality=94)
