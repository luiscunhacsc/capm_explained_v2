import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# CAPM calculation function
def calculate_capm(rf, beta, market_return):
    expected_return = rf + beta * (market_return - rf)
    market_risk_premium = market_return - rf
    return expected_return, market_risk_premium

# Reset parameters callback
def reset_parameters():
    st.session_state["rf_slider"] = 0.03
    st.session_state["beta_slider"] = 1.0
    st.session_state["market_slider"] = 0.08
    st.session_state["stock_return_slider"] = 0.10

# Lab parameter setters
def set_lab1_params():
    st.session_state["rf_slider"] = 0.02
    st.session_state["beta_slider"] = 0.5
    st.session_state["market_slider"] = 0.10
    st.session_state["stock_return_slider"] = 0.07

def set_lab2_params():
    st.session_state["rf_slider"] = 0.05
    st.session_state["beta_slider"] = -0.3
    st.session_state["market_slider"] = 0.08
    st.session_state["stock_return_slider"] = 0.04

def set_lab3_params():
    st.session_state["rf_slider"] = 0.03
    st.session_state["beta_slider"] = 1.5
    st.session_state["market_slider"] = 0.09
    st.session_state["stock_return_slider"] = 0.16

# Configure the app
st.set_page_config(layout="wide")
st.title("📈 Understanding CAPM: Capital Asset Pricing Model")
st.markdown("Explore the relationship between risk and expected return in financial markets")

# Sidebar
with st.sidebar:
    st.header("⚙️ Parameters")
    st.button("↺ Reset Defaults", on_click=reset_parameters)
    
    rf = st.slider("Risk-Free Rate (rf)", 0.0, 0.15, 0.03, key="rf_slider")
    beta = st.slider("Stock Beta (β)", -0.5, 2.5, 1.0, 0.1, key="beta_slider")
    market_return = st.slider("Expected Market Return (E(Rm))", 0.0, 0.20, 0.08, key="market_slider")
    stock_return = st.slider("Actual Stock Return", 0.0, 0.30, 0.10, key="stock_return_slider")

    # License and authorship
    st.markdown("---")
    st.markdown("""
    **⚠️ Disclaimer**  
    *Educational purposes only. No accuracy guarantees. Do not use this as an investment tool if you are not a qualified professional investor.*  
    
    <small>
    The author does not engage in stock trading and does not endorse it for non-professional investors. 
    All information provided is for educational purposes only and should not be construed as financial or 
    investment advice. Investing involves significant risks and may not be suitable for all investors. 
    Always consult a qualified financial professional before making any investment decisions.
    </small>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 20px;">
        <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.en" target="_blank">
            <img src="https://licensebuttons.net/l/by-nc/4.0/88x31.png" alt="CC BY-NC 4.0">
        </a>
        <br>
        <span style="font-size: 0.8em;">By Luís Simões da Cunha</span>
    </div>
    """, unsafe_allow_html=True)

# Main tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎮 Interactive Model", 
    "📚 Theoretical Framework",
    "🔬 Practical Labs", 
    "🧠 Core Concepts",
    "🏋️ Challenge Zone"
])

with tab1:
    # Calculate CAPM values
    exp_return, risk_premium = calculate_capm(rf, beta, market_return)
    alpha = stock_return - exp_return
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("CAPM Expected Return", f"{exp_return:.2%}", 
                 help="Theoretical return based on market conditions and stock risk")
        st.metric("Market Risk Premium", f"{risk_premium:.2%}",
                 help="Extra return investors demand for bearing market risk")
        st.metric("Alpha (Excess Return)", f"{alpha:.2%}", 
                 "Underperforming" if alpha < 0 else "Outperforming",
                 help="Real return minus expected return - measures stock performance")
        
        st.markdown("""
        **Live Insights:**
        - β < 1: Safer than market → Lower required return
        - β > 1: Riskier than market → Higher required return
        - α > 0: Beating market expectations
        """)

    with col2:
        # Security Market Line plot
        fig, ax = plt.subplots(figsize=(10, 6))
        betas = np.linspace(-0.5, 2.5, 50)
        returns = rf + betas * (market_return - rf)
        
        ax.plot(betas, returns, label='Security Market Line', color='navy', lw=2)
        ax.scatter([beta], [exp_return], color='red', s=100, 
                  label='Selected Stock', zorder=5)
        ax.scatter(1, market_return, color='green', s=100, 
                  marker='s', label='Market Portfolio', zorder=5)
        ax.axhline(y=rf, color='orange', linestyle='--', label='Risk-Free Rate')
        
        ax.set_title("Security Market Line (SML)", fontweight='bold')
        ax.set_xlabel("Beta (Systematic Risk)")
        ax.set_ylabel("Expected Return")
        ax.grid(True, alpha=0.3)
        ax.legend()
        st.pyplot(fig)

with tab2:
    st.markdown("""
    ## CAPM Theoretical Framework
    
    ### The Fundamental Formula
    $$
    E(R_i) = R_f + \\beta_i[E(R_m) - R_f]
    $$
    
    **Where:**
    - $E(R_i)$ = Expected return of investment
    - $R_f$ = Risk-free rate (e.g., government bonds)
    - $\\beta_i$ = Beta coefficient (measure of systematic risk)
    - $E(R_m)$ = Expected market return

    ### Key Components Explained
    
    **1. Risk-Free Rate (Rf):**  
    The return of "safe" investments with virtually no risk  
    *Example: 10-year US Treasury bonds yielding 3%*
    
    **2. Beta (β):**  
    Measures how much a stock moves with the market:  
    - β = 1: Moves with market  
    - β > 1: More volatile than market (Tech stocks)  
    - β < 1: Less volatile than market (Utilities)  
    - β = 0: No correlation (Rare)  
    - β < 0: Inverse correlation (Gold, some ETFs)
    
    **3. Market Risk Premium:**  
    The extra return investors demand for taking market risk  
    *Calculated as: E(Rm) - Rf*
    
    ### Why CAPM Matters
    - Helps determine if a stock is properly valued  
    - Guides portfolio construction  
    - Sets hurdle rates for corporate investments  
    - Foundation for modern portfolio theory
    """)

with tab3:
    st.header("🔬 Practical CAPM Labs")
    st.markdown("Learn through real-world scenarios - Use buttons to set lab parameters and explore!")
    
    lab = st.radio("Choose a Lab:", [
        "Lab 1: Defensive vs Aggressive Stocks",
        "Lab 2: Negative Beta Assets", 
        "Lab 3: Alpha Hunters"
    ])
    
    if lab == "Lab 1: Defensive vs Aggressive Stocks":
        st.subheader("🏦 Lab 1: Defensive vs Aggressive Stocks")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.button("⚡ Set Lab 1 Parameters", on_click=set_lab1_params)
            st.markdown("""
            **Scenario:**  
            Compare two stocks during market turbulence (+10% market return):
            - **Defensive Stock:** β=0.5 (Utilities)  
            - **Aggressive Stock:** β=1.5 (Tech Startup)
            
            **Tasks:**
            1. Calculate expected returns for both
            2. Determine which outperformed CAPM predictions
            3. Analyze risk-return tradeoff
            """)
        with col2:
            st.markdown("""
            **Analysis Guide:**
            1. Notice how β amplifies/reduces market returns  
            2. Defensive stocks protect in downturns but limit upside  
            3. High β stocks are "market amplifiers"
            
            **Reflection Questions:**
            - When would you prefer defensive stocks?  
            - Why might aggressive stocks underperform expectations?  
            - How does β affect portfolio diversification?
            """)
    
    elif lab == "Lab 2: Negative Beta Assets":
        st.subheader("💎 Lab 2: Negative Beta Assets")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.button("⚡ Set Lab 2 Parameters", on_click=set_lab2_params)
            st.markdown("""
            **Scenario:**  
            Explore a rare asset with β=-0.3 (Gold ETF) during:
            - Market return: 8%  
            - Actual return: 4%
            
            **Tasks:**
            1. Calculate expected return  
            2. Explain why α is positive/negative  
            3. Discuss uses in portfolio construction
            """)
        with col2:
            st.markdown("""
            **Key Insights:**
            - Negative β assets move opposite to market  
            - Provide "insurance" during market crashes  
            - Typically have lower expected returns
            
            **Real-World Examples:**
            - Gold  
            - Inverse ETFs  
            - Some consumer staples
            
            **Reflection Questions:**
            - Why are negative β assets rare?  
            - When would investors buy them?  
            - How do they affect portfolio risk?
            """)
    
    else:
        st.subheader("🔍 Lab 3: Alpha Hunters")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.button("⚡ Set Lab 3 Parameters", on_click=set_lab3_params)
            st.markdown("""
            **Scenario:**  
            Analyze a high-performing stock:
            - β=1.5  
            - Actual return=16%  
            - Market return=9%
            
            **Tasks:**
            1. Calculate expected return and α  
            2. Determine if over/undervalued  
            3. Discuss α persistence
            """)
        with col2:
            st.markdown("""
            **Alpha Insights:**
            - Positive α suggests outperformance  
            - Could indicate:
              - Superior management  
              - Market inefficiency  
              - Temporary luck
            
            **Fundamental Analysis:**
            - Compare α to industry averages  
            - Check α consistency over time  
            - Analyze financial ratios
            
            **Reflection Questions:**
            - Can α persist long-term?  
            - How efficient are markets really?  
            - What risks come with chasing α?
            """)

with tab4:
    st.markdown("""
    ## Core Financial Concepts
    
    ### Systematic vs. Unsystematic Risk
    **Systematic Risk (Market Risk):**  
    - Affects entire market (recessions, interest rates)  
    - Measured by β  
    - Cannot be diversified  
    - Compensated by market risk premium
    
    **Unsystematic Risk (Specific Risk):**  
    - Company-specific (management, products)  
    - Can be diversified away  
    - No compensation in CAPM
    
    ### Efficient Frontier & CML
    - **Capital Market Line (CML):** Optimal risk-return combinations  
    - **Market Portfolio:** Contains all risky assets  
    - **Sharpe Ratio:** Measures risk-adjusted returns
    
    ### CAPM Assumptions
    1. Rational investors  
    2. Single-period transactions  
    3. Frictionless markets  
    4. Unlimited borrowing/lending at Rf  
    5. Homogeneous expectations
    
    ### Practical Limitations
    - β estimates vary with time periods  
    - True market portfolio unobservable  
    - Ignores taxes and transaction costs  
    - Assumes normal return distribution
    """)

with tab5:
    st.markdown("""
    ## 🏋️ Challenge Zone
    
    ### Case Study: Portfolio Manager
    You manage €10M with:
    - Risk-free rate: 3%  
    - Market return: 10%  
    - Client requires 12% return
    
    **Tasks:**
    1. What β portfolio do you need?  
    2. How would you construct it?  
    3. What risks are you taking?
    
    ### Interactive Calculator
    """)
    challenge_rf = st.number_input("Challenge Risk-Free Rate", 0.0, 0.15, 0.03)
    challenge_market = st.number_input("Challenge Market Return", 0.0, 0.20, 0.10)
    challenge_target = st.number_input("Target Portfolio Return", 0.0, 0.30, 0.12)
    
    challenge_beta = (challenge_target - challenge_rf) / (challenge_market - challenge_rf)
    st.markdown(f"""
    **Required Beta:** {challenge_beta:.2f}
    
    **Interpretation:**  
    - β > 1: Need aggressive stocks  
    - β < 1: Can use leverage  
    - Reality Check: Very high β (>2) may be unrealistic
    """)

# Run with: streamlit run capm_app.py