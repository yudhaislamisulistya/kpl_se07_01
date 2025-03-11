from enum import Enum

# State
class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

# Trigger Input
class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    
# Transition
state_transitions = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    }
}

def change_state(current_state, trigger_input):
    if current_state in state_transitions and trigger_input in state_transitions[current_state]:
        # TERDAFTAR, AKTIF, LULUS, CUTI
        return state_transitions[current_state][trigger_input] 
    return "Transisi Tidak valid"

current_state = StudentStatusState.LULUS
trigger_input = TriggerInputState.MENGAJUKAN_CUTI

next_state = change_state(current_state, trigger_input)
print(next_state)