def tower(n:int, source:str, helper:str,target:str):
    if n==0:
        return
    tower(n-1, source,target,helper)
    print(f"Move disk {n} from {source} -> {target}")
    tower(n-1,helper,source,target)
if __name__ == "__main__":
    n=int(input("Enter the number of disks:"))
    print(f"\n Steps to solve Tower for {n} disks")
    tower(n,"A","B","C")
