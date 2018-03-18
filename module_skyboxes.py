####################################################################################################################
# The first "mesh_name" parameter is the name of the skybox mesh to be used for that entry.
# You can check our meshes from the "skyboxes.brf" file with OpenBRF and copy them, just replace the material's
# textures with yours; you will also have to change the specular color parameters for correct HDR rendering.
# Of course specular color does not correspond to specular lighting, those parameters are used as compression
# values for RGBE decoding and should be generated while you generate RGBE textures (specular.red = Scale component,
# specular.green = Bias component). You can check our materials for examples of this usage.
#
# For skybox textures, we are using uncompressed *.hdr files to generate *_rgb.dds and *_exp.dds files.
# It is just a RGBE encoding of the skybox for hdr lighting, here is an example:
# "skybox.dds": a simple non-hdr (LDR) image, used when you dont use hdr (DXT1 format is good).
# "skybox_rgb.dds": RGB components of the HDR image (DXT1 format is preferred).
# "skybox_exp.dds": E (exponent) component of the HDR image (L16 format is good, you can use half resolution for this texture).
# We use our own command line tool to generete those files from a "skybox.hdr" image, but you could generate
# them with a HDR image editor; the images should be gamma corrected and should not have mipmaps.
#
# Each skybox entry contains the following fields:
# 1) Mesh name.
# 2) Flags.
# 3) Sun heading.
# 4) Sun altitude.
# 5) Flare strength.
# 6) Post effects (postfx).
# 7) Sun color.
# 8) Hemi color.
# 9) Ambient color.
#   10.1) Fog start distance.
#   10.2) Fog color.
####################################################################################################################

sf_day        = 0x00000000
sf_dawn       = 0x00000001
sf_night      = 0x00000002
sf_mask       = 0x00000003 # Code from https://forums.taleworlds.com/index.php?topic=218069.0 Thanks to Xenoargh.

sf_clouds_0   = 0x00000000  # GCA 00-15
sf_clouds_1   = 0x00000010  # GCA 16-50
sf_clouds_2   = 0x00000020  # GCA 51-85
sf_clouds_3   = 0x00000030  # GCA 86-100

sf_no_shadows = 0x10000000  # Simply removes shadows
sf_HDR        = 0x20000000  # This will generate HDR-shaded skyboxes, you should make a LDR version of your skybox for compatibility

skyboxes = [
  ("sky_day_0a",   sf_day|sf_clouds_0,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0b",   sf_day|sf_clouds_0,   0.0, 42.0, 0.7, "pfx_sunny",    (240.0/62,220.0/62,110.0/62), (0.0, 0.0, 0.0), (040.0/255,060.0/255,100.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0c",   sf_day|sf_clouds_0,   0.0, 55.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,035.0/255,070.0/255), (100, 0xFF8CA2AD)),#

  ("sky_day_1a",   sf_day|sf_clouds_1,   0.0, 44.0, 1.0, "pfx_sunny",    (170.0/62,140.0/62,090.0/62), (0.0, 0.0, 0.0), (030.0/255,050.0/255,050.0/255), (100, 0xFF7B94A2)),#
  ("sky_day_1b",   sf_day|sf_clouds_1,   0.0, 48.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (020.0/255,035.0/255,045.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_1c",   sf_day|sf_clouds_1,   0.0, 55.0, 0.7, "pfx_sunny",    (216.0/62,185.0/62,117.0/62), (0.0, 0.0, 0.0), (091.0/255,105.0/255,115.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_1d",   sf_day|sf_clouds_1,   0.0, 58.0, 1.0, "pfx_sunny",    (190.0/62,170.0/62,130.0/62), (0.0, 0.0, 0.0), (015.0/255,030.0/255,040.0/255), (100, 0xFF52849E)),#

  ("sky_day_2a",   sf_day|sf_clouds_2,   0.0, 42.5, 0.5, "pfx_cloudy",   (170.0/62,150.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,035.0/255), (005, 0xFF78828C)),#
  ("sky_day_2b",   sf_day|sf_clouds_2,   0.0, 35.0, 0.4, "pfx_cloudy",   (100.0/62,090.0/62,070.0/62), (0.0, 0.0, 0.0), (040.0/255,040.0/255,040.0/255), (050, 0xFF9BA087)),#
  ("sky_day_2c",   sf_day|sf_clouds_2,   0.0, 30.0, 0.9, "pfx_cloudy",   (200.0/62,175.0/62,150.0/62), (0.0, 0.0, 0.0), (020.0/255,025.0/255,030.0/255), (300, 0xFF6E7882)),#
  ("sky_day_2d",   sf_day|sf_clouds_2,   0.0, 32.5, 0.3, "pfx_cloudy",   (160.0/62,140.0/62,110.0/62), (0.0, 0.0, 0.0), (015.0/255,020.0/255,030.0/255), (900, 0xFF8CA2AD)),#

  ("sky_day_3a",   sf_day|sf_clouds_3,   0.0, 17.0, 0.3, "pfx_overcast", (090.0/62,115.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,030.0/255,030.0/255), (300, 0xFF3C4646)),#
  ("sky_day_3b",   sf_day|sf_clouds_3,   0.0, 42.5, 0.2, "pfx_overcast", (070.0/62,110.0/62,130.0/62), (0.0, 0.0, 0.0), (008.0/255,035.0/255,084.0/255), (300, 0xFF788C96)),#
  ("sky_day_3c",   sf_day|sf_clouds_3,   0.0, 70.0, 0.0, "pfx_overcast", (090.0/62,110.0/62,110.0/62), (0.0, 0.0, 0.0), (008.0/255,008.0/255,008.0/255), (300, 0xFF464646)),#
  ("sky_day_3d",   sf_day|sf_clouds_3,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#

  ("sky_night_0a", sf_night|sf_clouds_0, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,010.0/62,040.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_1a", sf_night|sf_clouds_1, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,008.0/62,030.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_2a", sf_night|sf_clouds_2, 0.0, 51.0, 0.3, "pfx_night",    (001.0/62,003.0/62,007.0/62), (0.0, 0.0, 0.0), (000.0/255,001.0/255,004.0/255), (400, 0xFF00040A)),#
  ("sky_night_3a", sf_night|sf_clouds_3, 0.0, 51.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_3b", sf_night|sf_clouds_3, 0.0, 40.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#

  ("sky_dawn_0a",  sf_dawn|sf_clouds_0,  0.0, 04, 0.6,   "pfx_sunset",   (150.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (020.0/255,010.0/255,025.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_0b",  sf_dawn|sf_clouds_0,  0.0, 05, 0.6,   "pfx_sunset",   (240.0/62,090.0/62,040.0/62), (0.0, 0.0, 0.0), (035.0/255,015.0/255,040.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_1a",  sf_dawn|sf_clouds_1,  0.0, 10, 0.3,   "pfx_sunset",   (215.0/62,070.0/62,006.0/62), (0.0, 0.0, 0.0), (018.0/255,025.0/255,045.0/255), (50, 0xFF5D5B65)),#
  ("sky_dawn_1b",  sf_dawn|sf_clouds_1,  0.0, 24, 0.9,   "pfx_sunset",   (130.0/62,035.0/62,010.0/62), (0.0, 0.0, 0.0), (018.0/255,012.0/255,021.0/255), (50, 0xFF462323)),#
  ("sky_dawn_2a",  sf_dawn|sf_clouds_2,  0.0, 10, 0.1,   "pfx_sunset",   (172.0/62,059.0/62,026.0/62), (0.0, 0.0, 0.0), (037.0/255,018.0/255,047.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_3a",  sf_dawn|sf_clouds_3,  0.0, 07, 0.1,   "pfx_sunset",   (080.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (010.0/255,005.0/255,005.0/255), (50, 0xFFA08C5F)),#
  ("sky_dawn_3b",  sf_dawn|sf_clouds_3,  0.0, 05, 0.3,   "pfx_sunset",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#

  ("cwe_sky_cloud_1", sf_day|sf_clouds_0,   0.0, 44.0, 1.0, "pfx_sunny",    (170.0/62,140.0/62,090.0/62), (0.0, 0.0, 0.0), (030.0/255,050.0/255,050.0/255), (100, 0xFF7B94A2)),#
  ("cwe_sky_cloud_2", sf_day|sf_clouds_3,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#

#############################################################HDR-copy#############################################################################################################

  ("sky_day_0a",   sf_day|sf_clouds_0|sf_HDR,   0.0, 56.0, 1.0, "pfx_sunny",    (140.0/62,160.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,050.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0b",   sf_day|sf_clouds_0|sf_HDR,   0.0, 42.0, 0.7, "pfx_sunny",    (240.0/62,220.0/62,110.0/62), (0.0, 0.0, 0.0), (040.0/255,060.0/255,100.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_0c",   sf_day|sf_clouds_0|sf_HDR,   0.0, 55.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,035.0/255,070.0/255), (100, 0xFF8CA2AD)),#

  ("sky_day_1a",   sf_day|sf_clouds_1|sf_HDR,   0.0, 44.0, 1.0, "pfx_sunny",    (170.0/62,140.0/62,090.0/62), (0.0, 0.0, 0.0), (030.0/255,050.0/255,050.0/255), (000, 0xFF7B94A2)),#
  ("sky_day_1b",   sf_day|sf_clouds_1|sf_HDR,   0.0, 48.0, 1.0, "pfx_sunny",    (204.0/62,202.0/62,115.0/62), (0.0, 0.0, 0.0), (020.0/255,035.0/255,045.0/255), (100, 0xFF8CA2AD)),#
  ("sky_day_1c",   sf_day|sf_clouds_1|sf_HDR,   0.0, 55.0, 0.7, "pfx_sunny",    (216.0/62,185.0/62,117.0/62), (0.0, 0.0, 0.0), (091.0/255,105.0/255,115.0/255), (400, 0xFF8CA2AD)),#
  ("sky_day_1d",   sf_day|sf_clouds_1|sf_HDR,   0.0, 58.0, 1.0, "pfx_sunny",    (190.0/62,170.0/62,130.0/62), (0.0, 0.0, 0.0), (015.0/255,030.0/255,040.0/255), (999, 0xFF52849E)),#

  ("sky_day_2a",   sf_day|sf_clouds_2|sf_HDR,   0.0, 42.5, 0.5, "pfx_cloudy",   (170.0/62,150.0/62,100.0/62), (0.0, 0.0, 0.0), (020.0/255,030.0/255,035.0/255), (005, 0xFF78828C)),#
  ("sky_day_2b",   sf_day|sf_clouds_2|sf_HDR,   0.0, 35.0, 0.4, "pfx_cloudy",   (100.0/62,090.0/62,070.0/62), (0.0, 0.0, 0.0), (040.0/255,040.0/255,040.0/255), (050, 0xFF9BA087)),#
  ("sky_day_2c",   sf_day|sf_clouds_2|sf_HDR,   0.0, 30.0, 0.9, "pfx_cloudy",   (200.0/62,175.0/62,150.0/62), (0.0, 0.0, 0.0), (020.0/255,025.0/255,030.0/255), (300, 0xFF6E7882)),#
  ("sky_day_2d",   sf_day|sf_clouds_2|sf_HDR,   0.0, 32.5, 0.3, "pfx_cloudy",   (160.0/62,140.0/62,110.0/62), (0.0, 0.0, 0.0), (015.0/255,020.0/255,030.0/255), (900, 0xFF8CA2AD)),#

  ("sky_day_3a",   sf_day|sf_clouds_3|sf_HDR,   0.0, 17.0, 0.3, "pfx_overcast", (090.0/62,115.0/62,115.0/62), (0.0, 0.0, 0.0), (010.0/255,030.0/255,030.0/255), (300, 0xFF3C4646)),#
  ("sky_day_3b",   sf_day|sf_clouds_3|sf_HDR,   0.0, 42.5, 0.2, "pfx_overcast", (070.0/62,110.0/62,130.0/62), (0.0, 0.0, 0.0), (008.0/255,035.0/255,084.0/255), (300, 0xFF788C96)),#
  ("sky_day_3c",   sf_day|sf_clouds_3|sf_HDR,   0.0, 70.0, 0.0, "pfx_overcast", (090.0/62,110.0/62,110.0/62), (0.0, 0.0, 0.0), (008.0/255,008.0/255,008.0/255), (300, 0xFF464646)),#
  ("sky_day_3d",   sf_day|sf_clouds_3|sf_HDR,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#

  ("sky_night_0a", sf_night|sf_clouds_0|sf_HDR, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,010.0/62,040.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_1a", sf_night|sf_clouds_1|sf_HDR, 0.0, 35.0, 0.2, "pfx_night",    (000.0/62,008.0/62,030.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_2a", sf_night|sf_clouds_2|sf_HDR, 0.0, 51.0, 0.3, "pfx_night",    (001.0/62,003.0/62,007.0/62), (0.0, 0.0, 0.0), (000.0/255,001.0/255,004.0/255), (400, 0xFF00040A)),#
  ("sky_night_3a", sf_night|sf_clouds_3|sf_HDR, 0.0, 51.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#
  ("sky_night_3b", sf_night|sf_clouds_3|sf_HDR, 0.0, 40.0, 0.1, "pfx_night",    (000.0/62,005.0/62,015.0/62), (0.0, 0.0, 0.0), (000.0/255,002.0/255,008.0/255), (400, 0xFF00040A)),#

  ("sky_dawn_0a",  sf_dawn|sf_clouds_0|sf_HDR,  0.0, 4, 0.6,    "pfx_sunset",   (150.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (020.0/255,010.0/255,025.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_0b",  sf_dawn|sf_clouds_0|sf_HDR,  0.0, 5, 0.6,    "pfx_sunset",   (240.0/62,090.0/62,040.0/62), (0.0, 0.0, 0.0), (035.0/255,015.0/255,040.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_1a",  sf_dawn|sf_clouds_1|sf_HDR,  0.0, 10, 0.3,   "pfx_sunset",   (215.0/62,070.0/62,006.0/62), (0.0, 0.0, 0.0), (018.0/255,025.0/255,045.0/255), (50, 0xFF5D5B65)),#
  ("sky_dawn_1b",  sf_dawn|sf_clouds_1|sf_HDR,  0.0, 24, 0.9,   "pfx_sunset",   (130.0/62,035.0/62,010.0/62), (0.0, 0.0, 0.0), (018.0/255,012.0/255,021.0/255), (50, 0xFF462323)),#
  ("sky_dawn_2a",  sf_dawn|sf_clouds_2|sf_HDR,  0.0, 10, 0.1,   "pfx_sunset",   (172.0/62,059.0/62,026.0/62), (0.0, 0.0, 0.0), (037.0/255,018.0/255,047.0/255), (50, 0xFF5B3C3E)),#
  ("sky_dawn_3a",  sf_dawn|sf_clouds_3|sf_HDR,  0.0, 7, 0.1,    "pfx_sunset",   (080.0/62,020.0/62,000.0/62), (0.0, 0.0, 0.0), (010.0/255,005.0/255,005.0/255), (50, 0xFFA08C5F)),#
  ("sky_dawn_3b",  sf_dawn|sf_clouds_3|sf_HDR,  0.0, 5, 0.3,    "pfx_sunset",   (150.0/62,035.0/62,008.0/62), (0.0, 0.0, 0.0), (005.0/255,005.0/255,005.0/255), (50, 0xFF5B3C3E)),#

  ("cwe_sky_cloud_1", sf_day|sf_clouds_0|sf_HDR,   0.0, 44.0, 1.0, "pfx_sunny",    (170.0/62,140.0/62,090.0/62), (0.0, 0.0, 0.0), (030.0/255,050.0/255,050.0/255), (100, 0xFF7B94A2)),#
  ("cwe_sky_cloud_2", sf_day|sf_clouds_0|sf_HDR,   0.0, 80.0, 0.0, "pfx_overcast", (180.0/62,170.0/62,150.0/62), (0.0, 0.0, 0.0), (025.0/255,030.0/255,030.0/255), (300, 0xFF8C8778)),#
]
import process_operations as po

def process_entry(processor, txt_file, entry, index):
  txt_file.write("%s %d %f %f %f %s\r\n" % entry[0:6])
  txt_file.write(" %f %f %f " % entry[6])
  txt_file.write(" %f %f %f " % entry[7])
  txt_file.write(" %f %f %f " % entry[8])
  txt_file.write(" %f %d\r\n" % entry[9])

export = po.make_export(data=skyboxes, data_name="skyboxes", file_name="Data/skyboxes",
    header_format="%d\r\n", process_entry=process_entry)
