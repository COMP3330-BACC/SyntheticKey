import bpy
from os import listdir, path

raw_path = '/home/matt/UON/COMP3330/keyDS/raw/'
seg_path = '/home/matt/UON/COMP3330/keyDS/seg/'

render_layers = bpy.context.scene.render.layers

files = [f for f in listdir(raw_path) if path.isfile(path.join(raw_path, f))]
files.sort()

last_render = files[-1]
last_render_num = last_render[:last_render.rfind('.')]

filenum = int(last_render_num) + 1

for layer in render_layers:
    # disable all
    for l in render_layers:
        l.use = False

    # re-enable a single one that matched the condition
    layer.use = True

    if layer.name == 'Raw':
        bpy.data.scenes[
            'Scene'].render.filepath = raw_path + '{0:010}'.format(filenum)
    if layer.name == 'Segmentation':
        bpy.data.scenes[
            'Scene'].render.filepath = seg_path + '{0:010}'.format(filenum)

    # RENDER HERE

    bpy.ops.render.render(write_still=True)