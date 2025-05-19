import yfinance as yf

portfolio = {}

def is_valid_stock(symbol):
    try:
        info = yf.Ticker(symbol).info
        return "regularMarketPrice" in info
    except:
        return False

def add_stock():
    symbol = input("Enter stock symbol (e.g. AAPL ,TSLA ,GOOG ,MSFT ,AMZN): ").upper()
    if not is_valid_stock(symbol):
        print(f"⚠️  {symbol} is not a valid stock ticker.")
        return
    try:
        shares = int(input("Enter number of shares: "))
        if shares <= 0:
            print("❌ Number of shares must be positive.")
            return
    except ValueError:
        print("❌ Invalid number.")
        return
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"✅ Added {shares} shares of {symbol} to portfolio.")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑️ Removed {symbol} from portfolio.")
    else:
        print(f"⚠️  {symbol} not found in portfolio.")

def show_portfolio():
    if not portfolio:
        print("📂 Your portfolio is empty.")
        return

    print("\n📈 Current Portfolio Performance:")
    total_value = 0.0
    for symbol, shares in portfolio.items():
        try:
            stock = yf.Ticker(symbol)
            price = stock.info['regularMarketPrice']
            value = price * shares
            total_value += value
            print(f"🔹 {symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")
        except:
            print(f"⚠️ Could not retrieve data for {symbol}.")
    print(f"\n💰 Total Portfolio Value: ${total_value:.2f}")

def menu():
    while True:
        print("\n--- Stock Portfolio Menu ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

menu()
