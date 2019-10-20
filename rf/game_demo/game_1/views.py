from django.shortcuts import render
from django.http import HttpResponse

import json, copy

# Create your views here.

G = [
    [0, 0, 0, 0, 0],
    [0, 0, "X", 0, 0],
    [0, 0, "X", "*", 0],
    [0, 0, 0, 0, 0],
    [0, "X", 0, 0, 0],
]


AUTO_REFRESH = True
REFRESH_TIME= 0.001
NOW_POS = [0, 0]
N, M = 3,4

SUCCESS_NUM = 0
FAIL_NUM = 0
STEP_NUM = 0
DIR_DCIT = {
    "up" : (0, -1),
    "down" : (0, 1),
    "left" : (-1, 0),
    "right" : (1, 0)
}

def index(request):
    
    tmp = copy.deepcopy(G)
    tmp[NOW_POS[1]][NOW_POS[0]] = "A"

    data = {
        "graph" : tmp,
        "refresh_time" : REFRESH_TIME,
        "auto_refresh" : AUTO_REFRESH,
        "now_pos" : NOW_POS,
        "success_num" : SUCCESS_NUM,
        "fail_num"  : FAIL_NUM,
        "s_f_rate" : SUCCESS_NUM / (FAIL_NUM + 1),
        "step_num" : STEP_NUM,
        "effect_succ" : SUCCESS_NUM / (STEP_NUM + 1),
        
    }
    
    return render(request, 'index.html', data)
    #return HttpResponse("hello~python")


def game_tools(request):
    global NOW_POS, SUCCESS_NUM, FAIL_NUM, STEP_NUM

    if(request.method == "GET"):
        result = {
            "now_pos" : NOW_POS,
        }
        return HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json,charset=utf-8")
    
    elif(request.method == "POST"):
        result = {
            'status' : "SUCCESS"
        }

        op = request.POST['op']

        if(op == "get_position"):
            result["now_pos"] = NOW_POS
            return HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json,charset=utf-8")

        elif(op ==  "set_position"):
            dir = request.POST["dir"]
            STEP_NUM += 1

            if dir not in DIR_DCIT.keys():
                result['status'] = "FAIL"
                return HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json,charset=utf-8")

            NOW_POS[0] += DIR_DCIT[dir][0]
            NOW_POS[1] += DIR_DCIT[dir][1]

            if NOW_POS[0] >= M or NOW_POS[0] < 0 or NOW_POS[1] >= N or NOW_POS[1] < 0:
                NOW_POS[0] -= DIR_DCIT[dir][0]
                NOW_POS[1] -= DIR_DCIT[dir][1]

            done = False
            if G[NOW_POS[1]][NOW_POS[0]] == "*":
                reward = 1
                done = True
                SUCCESS_NUM += 1
            elif G[NOW_POS[1]][NOW_POS[0]] == "X":
                reward = -1
                done = True
                FAIL_NUM += 1
            else:
                reward = 0

            result['now_pos'] = NOW_POS
            result['reward'] = reward
            result['done'] = done

            return HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json,charset=utf-8")

        elif(op == "reset"):

            NOW_POS = [0, 0]
            result["now_pos"] = NOW_POS

            return HttpResponse(json.dumps(result, ensure_ascii=False),content_type="application/json,charset=utf-8")

