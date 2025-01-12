def solution(video_len, pos, op_start, op_end, commands):
    def skip(t):
        # 현재 위치가 오프닝 구간에 있는 경우 오프닝 끝 위치로 이동
        if op_start <= t <= op_end:
            return op_end
        return t

    def str2sec(s):
        # 문자열을 초 단위로 변환
        mm, ss = map(int, s.split(":"))
        return mm * 60 + ss

    def sec2str(t):
        # 초 단위를 문자열로 변환
        mm, ss = divmod(t, 60)
        return f'{mm:02d}:{ss:02d}'

    # 입력된 시간들을 초 단위로 변환
    video_len, pos, op_start, op_end = map(str2sec, [video_len, pos, op_start, op_end])

    # 시작 위치에서 오프닝 구간 확인
    pos = skip(pos)

    for command in commands:
        if command == "prev":
            # 10초 전으로 이동 (영상 시작 위치를 넘지 않음)
            pos = max(0, pos - 10)
        else:
            # 10초 후로 이동 (영상 끝 위치를 넘지 않음)
            pos = min(video_len, pos + 10)
        
        # 이동 후 오프닝 구간 확인
        pos = skip(pos)

    # 최종 위치를 문자열로 변환하여 반환
    return sec2str(pos)
