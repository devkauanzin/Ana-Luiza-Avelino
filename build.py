import base64
s=open('src.html').read()
for f,m in [('img/dra-circle.webp','image/webp'),('img/mural.webp','image/webp')]:
    s=s.replace(f'src="{f}"',f'src="data:{m};base64,'+base64.b64encode(open(f,'rb').read()).decode()+'"')
for f in ['img/fredoka.woff2','img/nunito.woff2']:
    s=s.replace(f'url({f})','url(data:font/woff2;base64,'+base64.b64encode(open(f,'rb').read()).decode()+')')
open('index.html','w').write(s); print(len(s))
