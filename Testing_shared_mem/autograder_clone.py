import os
import importlib.util
from multiprocessing.shared_memory import SharedMemory
from multiprocessing.shared_memory import ShareableList

dir_path = os.path.dirname(os.path.realpath(__file__))
specific = importlib.util.spec_from_file_location("assistant_clone", os.path.join(dir_path, "assistant_clone.py"))
assistant_clone = importlib.util.module_from_spec(specific)
specific.loader.exec_module(assistant_clone)

spec = importlib.util.spec_from_file_location("submission_clone", os.path.join(dir_path, "submission_clone.py"))
submission_clone = importlib.util.module_from_spec(spec)
spec.loader.exec_module(submission_clone)


def main():
    #print("making first list")
    stuff = ShareableList([1,2,3,4], name="mySharedList")
    inf = assistant_clone.is_inf(submission_clone.eat)

    if (inf == "All Good"):
        #assistant_clone.l_data = stuff
        print(submission_clone.eat())
    stuff.shm.close()
    stuff.shm.unlink()
    #print("finished first inf")

    try:
        stuff = ShareableList([1], name="myNewSharedList")
    except:
        print("PROBLEEEEEMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    #print("do we have stuff?", stuff[0])
    #print("creating new shared list")
    inf = assistant_clone.is_inf(submission_clone.add, (1,1))

    if (inf == "All Good"):
        #assistant_clone.l_data = [1]
        #shared_mem.buf[0] = 1
        print("setting")
        print(submission_clone.add(1,1))

    inf = assistant_clone.is_inf(submission_clone.test)

    if (inf == "All Good"):
        print(submission_clone.test())

    #shared_mem.close()

if __name__ == "__main__":
    main()
