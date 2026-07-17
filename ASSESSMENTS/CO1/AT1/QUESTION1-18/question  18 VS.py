question  18 


import math

# ---------------- Utility ----------------

def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

# ---------------- Recurrence ----------------

def T(n):
    if n <= 1:
        return 1
    return T(n//2) + math.log2(n)

# ---------------- Recursive Tree ----------------

def tree(n, prefix="", last=True):
    connector = "└── " if last else "├── "
    print(prefix + connector + f"T({n})")
    if n > 1:
        tree(n//2, prefix + ("    " if last else "│   "), True)

# ---------------- Dynamic Expansion ----------------

def expansion(n):
    print("\n==============================")
    print("INTERMEDIATE EXPANSIONS")
    print("==============================\n")

    cur = n
    logs = []

    while cur > 1:
        logs.append(f"log2({cur})")
        rhs = " + ".join(reversed(logs))
        print(f"T({n}) = T({cur//2}) + {rhs}")
        cur //= 2

    print(f"T({n}) = T(1) + " + " + ".join(reversed(logs)))

# ---------------- Mathematical Derivation ----------------

def derivation(n):
    k = int(math.log2(n))

    print("\n==============================")
    print("SUBSTITUTION METHOD")
    print("==============================\n")

    print("Given")
    print("T(n) = T(n/2) + log n\n")

    print("Expand repeatedly\n")
    print("T(n)")
    print("= T(n/2) + log n")
    print("= T(n/4) + log(n/2) + log n")
    print("= T(n/8) + log(n/4) + log(n/2) + log n")
    print("= ...")
    print("= T(1) + Σ log(n/2^i)\n")

    print("Since")
    print("log(n/2^i) = log(n) - i\n")

    print("Therefore")
    print("T(n)")
    print("= 1 + Σ(log(n)-i)")
    print("= 1 + (k+1)log(n) - Σi")
    print("= 1 + (k+1)log(n) - k(k+1)/2")
    print(f"\nWhere k = log2({n}) = {k}")
    print("\nIgnoring constants and lower-order terms")
    print("T(n) = Θ((log n)^2)")

# ---------------- Trace ----------------

def trace(n, depth=0):
    ind = "   "*depth
    if n <= 1:
        print(ind + "T(1)=1")
        return 1
    print(ind + f"T({n})")
    x = trace(n//2, depth+1)
    ans = x + math.log2(n)
    print(ind + f"Return T({n}) = {ans:.4f}")
    return ans

# ---------------- Search Simulation ----------------

def simulation(n):
    print("\n==============================")
    print("INTELLIGENT SEARCH SIMULATION")
    print("==============================\n")
    cur = n
    level = 0
    while cur >= 1:
        print(f"Level {level:2d} : Input Size = {cur:6d}", end="")
        if cur > 1:
            print(f"   Indexed Search Work = log2({cur}) = {math.log2(cur):.2f}")
        else:
            print("   Base Case")
        if cur == 1:
            break
        cur //= 2
        level += 1

# ---------------- Complexity ----------------

def complexity():
    print("\n==============================")
    print("COMPLEXITY ANALYSIS")
    print("==============================\n")
    print("Recurrence Relation")
    print("T(n) = T(n/2) + log n\n")
    print("Problem size reduces by half.")
    print("Recursion depth = Θ(log n)")
    print("Work at each level = Θ(log n)")
    print("Total work = Θ(log n) × Θ(log n)")
    print("Time Complexity = Θ((log n)^2)")
    print("Space Complexity = Θ(log n)\n")
    print("Best Case    : Θ((log n)^2)")
    print("Average Case : Θ((log n)^2)")
    print("Worst Case   : Θ((log n)^2)")

# ---------------- Efficiency ----------------

def efficiency():
    print("\n==============================")
    print("EFFICIENCY ANALYSIS")
    print("==============================\n")
    print("• The input size is halved at every recursive call.")
    print("• Hence only logarithmic recursion levels are created.")
    print("• Indexed search performs logarithmic work at each level.")
    print("• Overall work becomes (log n)^2.")
    print("• Growth is much slower than O(n) and O(n log n).")
    print("• Therefore the algorithm scales efficiently for large inputs.")

# ---------------- Final ----------------

def summary():
    print("\n==============================")
    print("FINAL RESULT")
    print("==============================\n")
    print("Recurrence        : T(n)=T(n/2)+log n")
    print("Recursive Levels  : Θ(log n)")
    print("Work Per Level    : Θ(log n)")
    print("Time Complexity   : Θ((log n)^2)")
    print("Space Complexity  : Θ(log n)")
    print("\nSuitable Applications")
    print("✓ Indexed Search")
    print("✓ Binary Search Variants")
    print("✓ Database Index Traversal")
    print("✓ Search Optimization Systems")

# ---------------- Main ----------------

print("="*60)
print("INTELLIGENT SEARCH OPTIMIZATION SYSTEM")
print("="*60)

n = int(input("Enter n (power of 2): "))

if not is_power_of_two(n):
    print("\nError: This proof assumes n is a power of 2 (2^k). Please enter a power of 2.")
else:
    simulation(n)

    print("\nRECURSIVE TREE\n")
    tree(n)

    expansion(n)

    derivation(n)

    print("\n==============================")
    print("RECURSIVE CALL TRACE")
    print("==============================\n")
    value = trace(n)

    print(f"\nComputed Value T({n}) = {value:.4f}")

    complexity()

    efficiency()

    summary()