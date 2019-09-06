from dataclasses import dataclass
from pathlib import Path
from os.path import realpath, dirname


@dataclass
class ProjectPath:
    __PROJECT_ROOT__ = Path(realpath(dirname(__file__)))
    __DATA_PATH__ = __PROJECT_ROOT__.joinpath('resource')


@dataclass
class WordCloudConfig:
    WC_DIR = ProjectPath.__DATA_PATH__.joinpath('word_cloud')
    PIC_PATH = WC_DIR.joinpath('WordCloud.png')
    MASK_PATH = WC_DIR.joinpath('mask_cloud.png')
    FONT = r'msjh.ttc'  # 微軟正黑體
    BG_COLOR = 'white'
    WITH_MASK = False

