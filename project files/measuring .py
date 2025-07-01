# Sample data: each country has some Economic Freedom indicators and GDP per capita
countries_data = [
    {
        "country": "Country A",
        "property_rights": 85,
        "gov_integrity": 80,
        "tax_burden": 70,
        "gov_spending": 60,
        "business_freedom": 75,
        "labor_freedom": 78,
        "monetary_freedom": 82,
        "trade_freedom": 79,
        "investment_freedom": 65,
        "financial_freedom": 68,
        "gdp_per_capita": 45000
    },
    {
        "country": "Country B",
        "property_rights": 40,
        "gov_integrity": 35,
        "tax_burden": 55,
        "gov_spending": 50,
        "business_freedom": 45,
        "labor_freedom": 52,
        "monetary_freedom": 49,
        "trade_freedom": 60,
        "investment_freedom": 40,
        "financial_freedom": 45,
        "gdp_per_capita": 12000
    },
    {
        "country": "Country C",
        "property_rights": 70,
        "gov_integrity": 68,
        "tax_burden": 62,
        "gov_spending": 58,
        "business_freedom": 72,
        "labor_freedom": 74,
        "monetary_freedom": 77,
        "trade_freedom": 75,
        "investment_freedom": 70,
        "financial_freedom": 73,
        "gdp_per_capita": 30000
    }
]

# Calculate Economic Freedom Score (mean of the 10 indicators)
def calculate_freedom_score(data):
    for country in data:
        indicators = [
            country["property_rights"],
            country["gov_integrity"],
            country["tax_burden"],
            country["gov_spending"],
            country["business_freedom"],
            country["labor_freedom"],
            country["monetary_freedom"],
            country["trade_freedom"],
            country["investment_freedom"],
            country["financial_freedom"]
        ]
        score = sum(indicators) / len(indicators)
        country["freedom_score"] = round(score, 2)

# Display results sorted by freedom score
def display_results(data):
    sorted_data = sorted(data, key=lambda x: x["freedom_score"], reverse=True)
    print("Country\t\tFreedom Score\tGDP per Capita")
    print("-" * 50)
    for c in sorted_data:
        print(f"{c['country']}\t{c['freedom_score']}\t\t${c['gdp_per_capita']:,}")

# Simple correlation check
def correlation_check(data):
    from math import sqrt
    def mean(vals): return sum(vals) / len(vals)
    def pearson_corr(x, y):
        x_mean, y_mean = mean(x), mean(y)
        numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
        denominator = sqrt(sum((xi - x_mean) ** 2 for xi in x)) * sqrt(sum((yi - y_mean) ** 2 for yi in y))
        return numerator / denominator if denominator else 0

    freedom_scores = [c["freedom_score"] for c in data]
    gdps = [c["gdp_per_capita"] for c in data]
    corr = pearson_corr(freedom_scores, gdps)
    print(f"\nCorrelation between Economic Freedom and GDP per Capita: {corr:.2f}")

# Run the analysis
calculate_freedom_score(countries_data)
display_results(countries_data)
correlation_check(countries_data)