from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    memo = [-1] * (length + 1)
    cuts = [-1] * (length + 1)

    def helper(n: int) -> int:
        if n == 0:
            return 0
        if memo[n] != -1:
            return memo[n]
        
        max_profit = 0
        for i in range(1, n + 1):
            profit = prices[i - 1] + helper(n - i)
            if profit > max_profit:
                max_profit = profit
                cuts[n] = i
        
        memo[n] = max_profit
        return max_profit

    max_profit = helper(length)

    # Відновлення розрізів
    cut_lengths = []
    n = length
    while n > 0:
        cut_lengths.append(cuts[n])
        n -= cuts[n]

    return {
        "max_profit": max_profit,
        "cuts": cut_lengths,
        "number_of_cuts": len(cut_lengths) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for length in range(1, length + 1):
        for cut in range(1, length + 1):
            if cut <= len(prices) and dp[length] < dp[length - cut] + prices[cut - 1]:
                dp[length] = dp[length - cut] + prices[cut - 1]
                cuts[length] = cuts[length - cut] + [cut]

    max_profit = dp[length]
    best_cuts = cuts[length]
    num_cuts = len(best_cuts) - 1 if sum(best_cuts) == length else len(best_cuts)

    best_cuts.sort(reverse=True)

    return {
        "max_profit": max_profit,
        "cuts": best_cuts,
        "number_of_cuts": num_cuts
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
