from enum import Enum,auto

class GameState(Enum):
    startscreen=auto()
    loadingscreen=auto()
    selectscreen=auto()

    #mod1
    mod1=auto()
    mod1_loading=auto()
    mod1_pause_screen=auto()

    #mod2
    mod2_set=auto()
    mod2_loading=auto()
    mod2_stage_1=auto()
    mod2_stage_2=auto()
    mod2_stage_3=auto()
    mod2_stage_4=auto()
    mod2_stage_5=auto()

    mod2_suc_1=auto()
    mod2_suc_2=auto()
    mod2_suc_3=auto()
    mod2_suc_4=auto()

    mod2_pause_screen=auto()

    #mod3
    mod3_set=auto()
    mod3_loading=auto()
    mod3_stage_1=auto()
    mod3_stage_2=auto()
    mod3_stage_3=auto()

    mod3_suc1=auto()
    mod3_suc2=auto()
    mod3_fail1=auto()
    mod3_fail2=auto()
    mod3_fail3=auto()

    mod3_pause_screen=auto()
    howtoplay=auto()
    ending_credit=auto()

State = GameState.startscreen

#모드 2 스테이지 잠금
lockevent=[False,False,False,False]
