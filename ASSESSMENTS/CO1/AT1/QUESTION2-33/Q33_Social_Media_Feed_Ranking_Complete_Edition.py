
"""
Q33 - FULL APPLICATION
Social Media Feed Ranking using Master Theorem
Recurrence: T(n)=4T(n/2)+n^2

Features
--------
1. Menu-driven application
2. Random social-media dataset generation
3. Feed statistics
4. Feed ranking
5. Search post by ID
6. Top-K posts
7. Recursive feed simulation
8. Recurrence expansion
9. Master theorem analysis
10. Recursion tree
11. Recursive trace
12. Scalability table
13. Performance comparison
14. Complexity analysis
15. Test cases
"""

import math
import random
from statistics import mean

def hr(): print("="*80)
def sr(): print("-"*80)

def power2(n): return n>0 and (n&(n-1))==0

def make_posts(n):
    random.seed(42)
    data=[]
    for i in range(1,n+1):
        likes=random.randint(50,500)
        comments=random.randint(0,120)
        shares=random.randint(0,80)
        views=random.randint(1000,20000)
        saves=random.randint(0,60)
        score=likes+2*comments+3*shares+views//100+2*saves
        data.append(dict(id=i,likes=likes,comments=comments,shares=shares,
                         views=views,saves=saves,score=score))
    return data

def table(posts,limit=15):
    print(f"{'ID':<5}{'Likes':<7}{'Com':<6}{'Share':<7}{'Views':<8}{'Save':<6}{'Score':<6}")
    for p in posts[:limit]:
        print(f"{p['id']:<5}{p['likes']:<7}{p['comments']:<6}{p['shares']:<7}{p['views']:<8}{p['saves']:<6}{p['score']:<6}")
    if len(posts)>limit: print("...")

def stats(posts):
    hr();print("DATASET STATISTICS");hr()
    print("Posts:",len(posts))
    print("Average Score:",round(mean([p["score"] for p in posts]),2))
    print("Maximum Score:",max(p["score"] for p in posts))
    print("Minimum Score:",min(p["score"] for p in posts))

def rank(posts):
    return sorted(posts,key=lambda x:x["score"],reverse=True)

def topk(posts,k=10):
    hr();print(f"TOP {k} POSTS");hr()
    for p in rank(posts)[:k]:
        print(f"Post {p['id']:>3} Score={p['score']}")

def search(posts,pid):
    hr();print("SEARCH RESULT");hr()
    for p in posts:
        if p["id"]==pid:
            print(p);return
    print("Post not found")

def recurrence(n):
    if n<=1:return 1
    return 4*recurrence(n//2)+n*n

def expansion(n):
    hr();print("RECURRENCE EXPANSION");hr()
    c=n;s=1
    while c>1:
        print(f"{s}. T({c}) = 4T({c//2}) + {c}²")
        c//=2;s+=1
    print("Base: T(1)=1")
    print("\nGeneral Form")
    print("T(n)=4^kT(n/2^k)+Σ4^i(n/2^i)^2")
    print("Each level contributes Θ(n²)")
    print("Levels = log₂n")
    print("Total = Θ(n² log n)")

def master():
    hr();print("MASTER THEOREM");hr()
    a,b=4,2
    print("a =",a)
    print("b =",b)
    print("f(n)=n²")
    print("n^(log_b(a)) = n^",int(math.log(a,b)),sep="")
    print("Case 1 : No")
    print("Case 2 : YES")
    print("Case 3 : No")
    print("Result : Θ(n² log n)")

def tree(n,d=0,m=3):
    print("   "*d+f"T({n})")
    if n<=1 or d>=m:return
    for _ in range(4):
        tree(n//2,d+1,m)

def trace(n,d=0):
    print("   "*d+f"Call T({n})")
    if n<=1:
        print("   "*d+"Return 1");return 1
    r=trace(n//2,d+1)
    ans=4*r+n*n
    print("   "*d+f"Return {ans}")
    return ans

def simulate(posts):
    hr();print("FEED RANKING SIMULATION");hr()
    cur=posts[:];lvl=0
    while True:
        r=rank(cur)
        print(f"Level {lvl}: Posts={len(cur)} Work={len(cur)**2}")
        print("Top IDs:",[x["id"] for x in r[:5]])
        if len(cur)==1:break
        cur=r[:max(1,len(cur)//2)]
        lvl+=1

def scalability():
    hr();print("SCALABILITY");hr()
    print(f"{'Posts':<8}{'n²':<12}{'Θ(n²logn)':<15}")
    for n in [16,32,64,128,256,512,1024,2048,4096]:
        print(f"{n:<8}{n*n:<12}{int(n*n*math.log2(n)):<15}")

def compare():
    hr();print("PERFORMANCE COMPARISON");hr()
    rows=[("Linear Ranking","Θ(n)"),
          ("Heap Ranking","Θ(n log n)"),
          ("Merge Sort","Θ(n log n)"),
          ("This Application","Θ(n² log n)")]
    for a,c in rows:
        print(f"{a:<30}{c}")

def complexity():
    hr();print("COMPLEXITY");hr()
    print("Best    : Θ(n² log n)")
    print("Average : Θ(n² log n)")
    print("Worst   : Θ(n² log n)")
    print("Space   : Θ(log n)")
    print("\nScalability Interpretation")
    print("* Four recursive subproblems.")
    print("* Quadratic ranking work each level.")
    print("* Logarithmic recursion depth.")
    print("* Efficient for moderate datasets but ranking cost grows quadratically.")

def tests():
    hr();print("TEST CASES");hr()
    for x in [1,2,4,8,16]:
        print(f"T({x}) = {recurrence(x)}")
    print("Input 3 -> Invalid")

def menu(posts,n):
    while True:
        hr()
        print("1.Display Posts")
        print("2.Dataset Statistics")
        print("3.Top 10 Posts")
        print("4.Search Post")
        print("5.Feed Simulation")
        print("6.Recurrence Expansion")
        print("7.Master Theorem")
        print("8.Recursion Tree")
        print("9.Recursive Trace")
        print("10.Scalability")
        print("11.Comparison")
        print("12.Complexity")
        print("13.Test Cases")
        print("14.Run Complete Demo")
        print("0.Exit")
        ch=input("Choice: ")
        if ch=="1": table(posts)
        elif ch=="2": stats(posts)
        elif ch=="3": topk(posts)
        elif ch=="4": search(posts,int(input("Post ID: ")))
        elif ch=="5": simulate(posts)
        elif ch=="6": expansion(n)
        elif ch=="7": master()
        elif ch=="8": hr();tree(min(n,8))
        elif ch=="9": hr();print("Value =",trace(n))
        elif ch=="10": scalability()
        elif ch=="11": compare()
        elif ch=="12": complexity()
        elif ch=="13": tests()
        elif ch=="14":
            table(posts);stats(posts);topk(posts);simulate(posts)
            expansion(n);master();hr();tree(min(n,8));hr()
            print("Value =",trace(n));scalability();compare();complexity();tests()
        elif ch=="0":
            break

def main():
    hr()
    print("SOCIAL MEDIA FEED RANKING SYSTEM")
    print("T(n)=4T(n/2)+n²")
    hr()
    n=int(input("Enter number of posts (power of 2): "))
    if not power2(n):
        print("Invalid input.");return
    posts=make_posts(n)
    menu(posts,n)

if __name__=="__main__":
    main()
