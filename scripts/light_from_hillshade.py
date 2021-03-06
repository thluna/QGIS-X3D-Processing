'''
QGIS Processing script
(c) 2017 Andreas Plesch
constructs directional light from azimuth and altitude
optionally skips light generation if only headlight is requested
'''
##X3D=group
##light from hillshade=name
##azimuth=number 315
##altitude=number 45
##multidirectional=number 0
##only_headlight=boolean false
##ambientIntensity=number 0.5
##intensity=number 0.5
##output_X3D_light=output string

out = '<Transform rotation="0 1 0 %s">\n'
out+= '    <Transform rotation="1 0 0 %s">\n'
out+= '        <DirectionalLight intensity="%s" ambientIntensity="%s" global="true"/>\n'
out+= '    </Transform>\n'
out+= '</Transform>\n'

d2r = 3.141592 / 180

a = 180/4 * d2r
mI = intensity/4
maI = ambientIntensity/4

az = 3.141592 - azimuth * d2r
al = -altitude * d2r

g = '<Group DEF="lights">\n'
if not only_headlight:
    light = out % (az, al, intensity, ambientIntensity)
    if multidirectional:
        light = out % (az - 1.5*a, al, mI, maI)
        light+= out % (az - 0.5*a, al, mI, maI)
        light+= out % (az + 0.5*a, al, mI, maI)
        light+= out % (az + 1.5*a, al, mI, maI)
    g+= light
g+= '</Group>\n'
output_X3D_light = g
#print(g)