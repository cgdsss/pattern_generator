from fpdf import FPDF
import yaml
import os

current_path = os.path.abspath(os.path.dirname(__file__))
stream = file(os.path.join(current_path, 'cfg.yaml'), 'r')
cfg = yaml.load(stream)

tag_type = cfg['tag_type']
tags_pose = cfg['tags_pose']
tags_id = cfg['tags_id']
tags_size = cfg['tags_size']
pdf_size = cfg['pdf_size']

pdf = FPDF(orientation = 'P', unit = 'cm', format=(pdf_size[0]*100.0, pdf_size[1]*100.0))
pdf.add_page()
print "Drawing: "
for i in range(len(tags_id)):
    print "--"
    print "id: ", str(tags_id[i])
    print "size: {0}m".format(tags_size[i])
    print "position: {0}m, {1}m".format(tags_pose[i][0], tags_pose[i][1])
    img = os.path.join(current_path, 'png/' + tag_type + "/" + str(tags_id[i]) + ".png")
    pdf.image(img, ((tags_pose[i][0] - tags_size[i] / 2.0) + pdf_size[0]/2.0) * 100.0,
        ((-tags_pose[i][1] - tags_size[i] / 2.0) + pdf_size[1]/2.0) * 100.0,
        tags_size[i] * 100.0, tags_size[i] * 100.0)
pdf_file = os.path.join(current_path, 'pattern.pdf')
pdf.output(pdf_file, 'F')
print "Done."
print "Already generated:", pdf_file