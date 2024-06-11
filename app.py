from mainframe import mainFrame
import argparse


if __name__ == '__main__':
    # 创建命令行
    parser = argparse.ArgumentParser()
    # 创建参数
    parser.add_argument("--model_path", type=str, default="../../model/mnist/swin_v2_b.pth")
    parser.add_argument("--resize", type=int, default=224)
    parser.add_argument("--window_w", type=int, default=800)
    parser.add_argument("--window_h", type=int, default=500)
    parser.add_argument("--mode", type=int, default=1)
    parser.add_argument("--img_size", type=int, default=448)
    # 解析命令行
    opt = parser.parse_args()
    # 创建窗口实例
    windows = mainFrame(opt)
    windows.winShow()
