import pygame
from pygame.locals import *
from sys import exit
from consts import *
from gobang import GoBang
from render import GameRender

# from gobang_ai import GobangAI

if __name__ == '__main__':
    gobang = GoBang()
    render = GameRender(gobang)
    # 先给AI留个接口
    # ai = GobangAI(gobang, ChessboardState.WHITE)
    result = ChessboardState.EMPTY
    enable_ai = False

    while True:
        # 捕捉pygame事件
        for event in pygame.event.get():
            # 退出程序
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                # 成功着棋
                if render.one_step():
                    result = gobang.get_chess_result()
                else:
                    continue
                if result != ChessboardState.EMPTY:
                    break
                if enable_ai:
                    # ai.one_step()
                    result = gobang.get_chess_result()
                else:
                    render.change_state()

        # 绘制
        render.draw_chess()
        render.draw_mouse()

        if result != ChessboardState.EMPTY:
            render.draw_result(result)

        # 刷新
        pygame.display.update()
