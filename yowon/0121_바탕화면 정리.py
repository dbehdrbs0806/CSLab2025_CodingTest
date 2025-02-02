def solution(wallpaper):
    # 초기값 설정
    min_row = float('inf')
    max_row = -float('inf')
    min_col = float('inf')
    max_col = -float('inf')

    # 파일 위치(#) 탐색
    for row_idx, row in enumerate(wallpaper):
        for col_idx, cell in enumerate(row):
            if cell == '#':
                min_row = min(min_row, row_idx)
                max_row = max(max_row, row_idx)
                min_col = min(min_col, col_idx)
                max_col = max(max_col, col_idx)

    # 드래그의 시작점과 끝점 계산
    lux, luy = min_row, min_col
    rdx, rdy = max_row + 1, max_col + 1

    return [lux, luy, rdx, rdy]
