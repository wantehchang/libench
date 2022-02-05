import unittest
import os
import make_page


class MakePageTest(unittest.TestCase):

  BUILD_DIR = "build/python_test"

  def setUp(self):
    os.makedirs(MakePageTest.BUILD_DIR, exist_ok=True)

  def test_make(self):
    image = make_page.Image(name="rgba")
    image.codecs.extend((
      make_page.Codec(name="HT", coding_efficiency="0.5", encode_time="0.5", decode_time="0.1"),
      make_page.Codec(name="J2K1", coding_efficiency="0.5", encode_time="0.5", decode_time="0.1")
    ))

    make_page.build(MakePageTest.BUILD_DIR, [image])
