from flask import Flask, render_template, request, jsonify
from flask import request
from datetime import datetime

app = Flask(__name__)

# Set global template variables for SEO
@app.context_processor
def inject_seo():
    return {
        'current_year': datetime.now().year,
        'site_name': 'Calculator Suite',
        'site_description': 'Comprehensive collection of free online calculators for construction, education, health, finance, and more.',
        'base_url': 'https://yourcalculatorwebsite.com',  # Change to your actual domain
        'author': 'Your Name or Company',
        'keywords': 'calculators, construction calculator, finance calculator, health calculator, education calculator'
    }

@app.route('/')
def index():
    return render_template('index.html', 
                         title='Free Online Calculators - Construction, Finance, Health & More',
                         description='Access our complete suite of free online calculators for construction, education, health monitoring, financial planning, and academic assessments.')

@app.route('/board-foot')
def board_foot():
    return render_template('board_foot.html', 
                         title='Board Foot Calculator - Lumber Measurement Tool',
                         description='Calculate board feet for lumber and wood materials quickly with our free online board foot calculator.')

@app.route('/stone')
def stone():
    return render_template('stone.html', 
                         title='Stone Calculator - Estimate Stone Material Needs',
                         description='Accurately estimate the amount of stone needed for your landscaping or construction project with our free stone calculator.')

@app.route('/gravel')
def gravel():
    return render_template('gravel.html', 
                         title='Gravel Calculator - Estimate Gravel Quantities',
                         description='Calculate how much gravel you need for your driveway, pathway, or construction project with our free gravel calculator.')

@app.route('/sand')
def sand():
    return render_template('sand.html', 
                         title='Sand Calculator - Estimate Sand Volume',
                         description='Determine the exact amount of sand required for your project with our free online sand calculator.')

@app.route('/tank-volume')
def tank_volume():
    return render_template('tank_volume.html', 
                         title='Tank Volume Calculator - Liquid Capacity Tool',
                         description='Calculate the volume of cylindrical, rectangular, or other shaped tanks with our free tank volume calculator.')

@app.route('/concrete')
def concrete():
    return render_template('concrete.html', 
                         title='Concrete Calculator - Estimate Concrete Yardage',
                         description='Determine how much concrete you need for slabs, footings, columns with our free concrete calculator.')

@app.route('/drywall-calculator')
def drywall_calculator():
    return render_template('drywall_calculator.html', 
                         title='Drywall Calculator - Sheetrock Estimation Tool',
                         description='Estimate drywall sheets, screws, and joint compound needed for your project with our free drywall calculator.')

@app.route('/rebar-calculator')
def rebar_calculator():
    return render_template('rebar_calculator.html', 
                         title='Rebar Calculator - Steel Reinforcement Estimator',
                         description='Calculate rebar spacing, quantities, and costs for concrete reinforcement with our free rebar calculator.')

@app.route('/roofing-calculator')
def roofing_calculator():
    return render_template('roofing_calculator.html', 
                         title='Roofing Calculator - Shingle & Material Estimator',
                         description='Estimate roofing materials, shingles, and costs for your roofing project with our free calculator.')

@app.route('/paver-calculator')
def paver_calculator():
    return render_template('paver_calculator.html', 
                         title='Paver Calculator - Patio & Walkway Estimator',
                         description='Calculate the number of pavers, sand, and base materials needed for your patio or walkway project.')

@app.route('/framing-calculator')
def framing_calculator():
    return render_template('framing.html', 
                         title='Framing Calculator - Wood Stud Calculation Tool',
                         description='Calculate stud spacing, lumber quantities, and framing costs for your construction project.')

@app.route('/gpa-calculator')
def gpa_calculator():
    return render_template('gpa-calculator.html', 
                         title='GPA Calculator - Grade Point Average Tool',
                         description='Calculate your current or cumulative GPA with our free online GPA calculator for high school and college students.')

@app.route('/apush-calculator')
def apush_calculator():
    return render_template('apush-calculator.html', 
                         title='APUSH Score Calculator - AP US History Exam',
                         description='Estimate your AP US History exam score with our free APUSH calculator based on multiple choice and essay sections.')

@app.route('/ap-lang-calculator')
def ap_lang_calculator():
    return render_template('ap-lang-calculator.html', 
                         title='AP Lang Calculator - AP English Language Score',
                         description='Calculate your potential AP English Language and Composition exam score with our free tool.')

@app.route('/lsat-calculator')
def lsat_calculator():
    return render_template('lsat-calculator.html', 
                         title='LSAT Score Calculator - Law School Admission',
                         description='Estimate your LSAT score based on practice test performance with our free LSAT calculator.')

@app.route('/digital-sat-calculator')
def digital_sat_calculator():
    return render_template('digital-sat-calculator.html', 
                         title='Digital SAT Calculator - New SAT Score Estimation',
                         description='Calculate your digital SAT score based on section performance with our free SAT calculator tool.')

@app.route('/lsac-gpa-calculator')
def lsac_gpa_calculator():
    return render_template('lsac-gpa-calculator.html', 
                         title='LSAC GPA Calculator - Law School Admission GPA',
                         description='Calculate your LSAC GPA for law school applications with our free calculator that follows official LSAC methodology.')

@app.route('/ib-grade-calculator')
def ib_grade_calculator():
    return render_template('ib-grade-calculator.html', 
                         title='IB Grade Calculator - International Baccalaureate',
                         description='Calculate your International Baccalaureate (IB) grades and predicted scores with our free IB calculator.')

@app.route('/waist-hip-ratio')
def waist_hip_ratio():
    return render_template('waist_hip_ratio.html', 
                         title='Waist to Hip Ratio Calculator - Health Assessment',
                         description='Calculate your waist-to-hip ratio (WHR) to assess health risks and body fat distribution with our free tool.')

@app.route('/fasting-calculator')
def fasting_calculator():
    return render_template('fasting_calculator.html', 
                         title='Fasting Calculator - Intermittent Fasting Planner',
                         description='Plan your intermittent fasting schedule and track fasting windows with our free fasting calculator.')

@app.route('/anc-calculator')
def anc_calculator():
    return render_template('anc_calculator.html', 
                         title='ANC Calculator - Absolute Neutrophil Count',
                         description='Calculate Absolute Neutrophil Count (ANC) from blood test results with our free medical calculator.')

@app.route('/homa-ir-calculator')
def homa_ir_calculator():
    return render_template('homa_ir_calculator.html', 
                         title='HOMA-IR Calculator - Insulin Resistance Tool',
                         description='Assess insulin resistance with our free HOMA-IR calculator using fasting glucose and insulin levels.')

@app.route('/steroid-conversion-calculator')
def steroid_conversion_calculator():
    return render_template('steroid_conversion_calculator.html', 
                         title='Steroid Conversion Calculator - Equivalent Doses',
                         description='Convert between different steroid medications and calculate equivalent doses with our free medical calculator.')

@app.route('/bmi-calculator')
def bmi_calculator():
    return render_template('bmi_calculator.html', 
                         title='BMI Calculator - Body Mass Index Tool',
                         description='Calculate your Body Mass Index (BMI) and learn about healthy weight ranges with our free calculator.')

@app.route('/0-60-calculator')
def zero_to_sixty_calculator():
    return render_template('0_60_calculator.html', 
                         title='0-60 Calculator - Car Acceleration Estimator',
                         description='Estimate your vehicle\'s 0-60 mph acceleration time based on weight and horsepower with our free calculator.')

@app.route('/quarter-mile-calculator')
def quarter_mile_calculator():
    return render_template('quarter_mile_calculator.html', 
                         title='Quarter Mile Calculator - Drag Racing Estimator',
                         description='Calculate quarter mile times and trap speeds for your vehicle based on power and weight.')

@app.route('/pregnancy-calculator')
def pregnancy_calculator():
    return render_template('pregnancy_calculator.html', 
                         title='Pregnancy Calculator - Due Date Estimator',
                         description='Estimate your due date, track pregnancy milestones, and calculate important dates with our free pregnancy calculator.')

@app.route('/engine-displacement-calculator')
def engine_displacement_calculator():
    return render_template('engine_displacement_calculator.html', 
                         title='Engine Displacement Calculator - CID & Liters',
                         description='Calculate engine displacement in cubic inches or liters based on bore, stroke, and cylinder count.')

@app.route('/towing-estimate-calculator')
def towing_estimate_calculator():
    return render_template('towing_estimate_calculator.html', 
                         title='Towing Calculator - Estimate Towing Capacity',
                         description='Estimate your vehicle\'s towing capacity and calculate tongue weight with our free towing calculator.')

@app.route('/power-to-weight-calculator')
def power_to_weight_calculator():
    return render_template('power_to_weight_calculator.html', 
                         title='Power to Weight Ratio Calculator - HP per Pound',
                         description='Calculate power-to-weight ratio for vehicles in hp/lb or hp/ton with our free calculator.')

@app.route('/gear-ratio-calculator')
def gear_ratio_calculator():
    return render_template('gear_ratio_calculator.html', 
                         title='Gear Ratio Calculator - RPM & Speed Estimator',
                         description='Calculate gear ratios, RPM at speed, and final drive ratios with our free automotive calculator.')

@app.route('/beam-calculator')
def beam_calculator():
    return render_template('beam_calculator.html', 
                         title='Beam Calculator - Load Capacity Estimator',
                         description='Calculate beam loads, spans, and deflection for construction projects with our free engineering tool.')

@app.route('/moment-of-inertia-calculator')
def moment_of_inertia_calculator():
    return render_template('moment_of_inertia_calculator.html', 
                         title='Moment of Inertia Calculator - Beam Analysis',
                         description='Calculate moment of inertia for various beam cross-sections with our free engineering calculator.')

@app.route('/ohio-paycheck-calculator')
def ohio_paycheck_calculator():
    return render_template('ohio_paycheck_calculator.html', 
                         title='Ohio Paycheck Calculator - Take Home Pay',
                         description='Calculate your Ohio take-home pay after taxes, deductions, and withholdings with our free paycheck calculator.')

@app.route('/michigan-paycheck-calculator')
def michigan_paycheck_calculator():
    return render_template('michigan_paycheck_calculator.html', 
                         title='Michigan Paycheck Calculator - Net Pay Estimator',
                         description='Estimate your Michigan paycheck after state and federal taxes with our free take-home pay calculator.')

@app.route('/nj-paycheck-calculator')
def nj_paycheck_calculator():
    return render_template('nj_paycheck_calculator.html', 
                         title='New Jersey Paycheck Calculator - Net Pay',
                         description='Calculate your New Jersey take-home pay after state and federal taxes with our free paycheck calculator.')

@app.route('/virginia-paycheck-calculator')
def virginia_paycheck_calculator():
    return render_template('virginia_paycheck_calculator.html', 
                         title='Virginia Paycheck Calculator - Salary After Taxes',
                         description='Estimate your Virginia paycheck after state and federal tax withholdings with our free calculator.')

@app.route('/colorado-paycheck-calculator')
def colorado_paycheck_calculator():
    return render_template('colorado_paycheck_calculator.html', 
                         title='Colorado Paycheck Calculator - Net Salary',
                         description='Calculate your Colorado take-home pay after taxes and deductions with our free paycheck estimator.')

@app.route('/texas-paycheck-calculator')
def texas_paycheck_calculator():
    return render_template('texas_paycheck_calculator.html', 
                         title='Texas Paycheck Calculator - No State Income Tax',
                         description='Calculate your Texas paycheck with no state income tax, estimating federal withholdings and deductions.')

@app.route('/hsa-calculator')
def hsa_calculator():
    return render_template('hsa_calculator.html', 
                         title='HSA Calculator - Health Savings Account',
                         description='Calculate HSA contributions, tax savings, and growth projections with our free Health Savings Account calculator.')

@app.route('/bonus-calculator')
def bonus_calculator():
    return render_template('bonus_calculator.html', 
                         title='Bonus Tax Calculator - Net Bonus Pay',
                         description='Calculate how much of your bonus you\'ll take home after taxes with our free bonus paycheck calculator.')

@app.route('/child-support-calculator')
def child_support_calculator():
    return render_template('child_support_calculator.html', 
                         title='Child Support Calculator - Estimate Payments',
                         description='Estimate child support payments based on income, custody arrangements, and state guidelines.')

@app.route('/reverse-tax-calculator')
def reverse_tax_calculator():
    return render_template('reverse_tax_calculator.html', 
                         title='Reverse Tax Calculator - Gross Pay Needed',
                         description='Calculate the gross pay needed to achieve a specific net pay amount after taxes with our reverse tax calculator.')

@app.route('/cash-on-cash-return')
def cash_on_cash_return():
    return render_template('cash_on_cash_return.html', 
                         title='Cash on Cash Return Calculator - Real Estate',
                         description='Calculate cash-on-cash return for real estate investments based on annual cash flow and initial investment.')

@app.route('/heloc-calculator')
def heloc_calculator():
    return render_template('heloc_calculator.html', 
                         title='HELOC Calculator - Home Equity Line of Credit',
                         description='Calculate payments, draw periods, and repayment terms for a Home Equity Line of Credit (HELOC).')

@app.route('/rref-calculator')
def rref_calculator():
    return render_template('rref_calculator.html', 
                         title='RREF Calculator - Reduced Row Echelon Form',
                         description='Transform matrices to reduced row echelon form (RREF) with our free online matrix calculator.')

@app.route('/matrix-calculator')
def matrix_calculator():
    return render_template('matrix_calculator.html', 
                         title='Matrix Calculator - Linear Algebra Tool',
                         description='Perform matrix operations including addition, multiplication, determinants, and inverses with our free calculator.')

@app.route('/mortgage-recast-calculator')
def mortgage_recast_calculator():
    return render_template('mortgage_recast_calculator.html', 
                         title='Mortgage Recast Calculator - Payment Reduction',
                         description='Calculate how a mortgage recast can lower your monthly payments after a lump sum payment.')

@app.route('/construction-loan-calculator')
def construction_loan_calculator():
    return render_template('construction_loan_calculator.html', 
                         title='Construction Loan Calculator - Draw Schedule',
                         description='Estimate payments and plan draw schedules for construction loans with our free calculator.')

@app.route('/dscr-loan-calculator')
def dscr_loan_calculator():
    return render_template('dscr_loan_calculator.html', 
                         title='DSCR Loan Calculator - Debt Service Coverage',
                         calculate='Calculate Debt Service Coverage Ratio (DSCR) for commercial real estate loans and investments.')

@app.route('/biweekly-mortgage-calculator')
def biweekly_mortgage_calculator():
    return render_template('biweekly_mortgage_calculator.html', 
                         title='Biweekly Mortgage Calculator - Early Payoff',
                         description='Calculate how biweekly mortgage payments can help pay off your loan faster and save on interest.')

@app.route('/usda-mortgage-calculator')
def usda_mortgage_calculator():
    return render_template('usda_mortgage_calculator.html', 
                         title='USDA Mortgage Calculator - Rural Housing Loan',
                         description='Calculate payments for USDA rural housing loans including principal, interest, insurance, and fees.')

@app.route('/early-payoff-calculator')
def early_payoff_calculator():
    return render_template('early_payoff_calculator.html', 
                         title='Early Mortgage Payoff Calculator - Savings',
                         description='Calculate how extra payments can help pay off your mortgage early and save on total interest.')

@app.route('/eigenvalue-calculator')
def eigenvalue_calculator():
    return render_template('eigenvalue_calculator.html', 
                         title='Eigenvalue Calculator - Matrix Eigenvalues',
                         description='Calculate eigenvalues and eigenvectors for 2x2, 3x3, or 4x4 matrices with our free linear algebra tool.')

@app.route('/gaussian-elimination')
def gaussian_elimination():
    return render_template('gaussian_elimination.html', 
                         title='Gaussian Elimination Calculator - Linear Systems',
                         description='Solve systems of linear equations using Gaussian elimination with our free step-by-step calculator.')

@app.route('/fourier-transform')
def fourier_transform():
    return render_template('fourier_transform.html', 
                         title='Fourier Transform Calculator - Signal Analysis',
                         description='Compute discrete Fourier transforms (DFT) for signal processing and analysis with our free calculator.')

@app.route('/quadratic-regression')
def quadratic_regression():
    return render_template('quadratic_regression.html', 
                         title='Quadratic Regression Calculator - Curve Fitting',
                         description='Perform quadratic regression to find the parabola of best fit for your data points.')

@app.route('/discriminant-calculator')
def discriminant_calculator():
    return render_template('discriminant_calculator.html', 
                         title='Discriminant Calculator - Quadratic Equations',
                         description='Calculate the discriminant of quadratic equations to determine the nature of roots with our free tool.')

@app.route('/Cubic-Yard-Calculator')
def Cubic_Yard_Calculator():
    return render_template('Cubic_Yard_Calculator.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy.html')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms.html')

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@app.route('/sitemap.xml')
def serve_sitemap():
    return render_template('sitemap.xml')

@app.route('/robots.txt')
def serve_robots():
    return render_template('robots.txt')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        length = float(data['length'])
        width = float(data['width'])
        depth = float(data['depth'])
        unit = data['unit']
        
        # Convert inches to feet if necessary
        if unit == 'inches':
            depth = depth / 12
        
        # Calculate cubic yards
        cubic_yards = (length * width * depth) / 27
        
        return jsonify({
            'success': True,
            'result': round(cubic_yards, 2)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
