import pytest
from moviepy.editor import *
import moviepy.video.tools.cuts as cuts

import sys
sys.path.append("tests")
import download_media

def test_download_media(capsys):
    with capsys.disabled():
       download_media.download()

def test_matplotlib():
    #for now, python 3.5 installs a version of matplotlib that complains
    #about $DISPLAY variable, so lets just ignore for now.
    if sys.version_info < (3,4):
       return

    if sys.version_info.major == 3 and sys.version_info.minor == 5:
       return

    import matplotlib.pyplot as plt
    import numpy as np
    from moviepy.editor import VideoClip
    from moviepy.video.io.bindings import mplfig_to_npimage

    x = np.linspace(-2, 2, 200)

    duration = 2

    fig, ax = plt.subplots()

    def make_frame(t):
        ax.clear()
        ax.plot(x, np.sinc(x**2) + np.sin(x + 2*np.pi/duration * t), lw=3)
        ax.set_ylim(-1.5, 2.5)
        return mplfig_to_npimage(fig)

    animation = VideoClip(make_frame, duration=duration)
    animation.write_gif('/tmp/matplotlib.gif', fps=20)


if __name__ == '__main__':
   pytest.main()
