from pydantic import BaseModel
from typing import Optional

# 基础信息 https://tushare.pro/document/2?doc_id=25
class StockListParams(BaseModel):
    ts_code: Optional[str] = None  # TS股票代码
    name: Optional[str] = None  # 名称
    market: Optional[str] = None  # 市场类别 （主板/创业板/科创板/CDR/北交所）
    list_status: Optional[str] = None  # 上市状态 L上市 D退市 P暂停上市，默认是L
    exchange: Optional[str] = None  # 交易所 SSE上交所 SZSE深交所 BSE北交所
    is_hs: Optional[str] = None  # 是否沪深港通标的，N否 H沪股通 S深股通

class StockListFields(BaseModel):
    ts_code: str  # TS代码
    symbol: str  # 股票代码
    name: str  # 股票名称
    area: str  # 地域
    industry: str  # 所属行业
    fullname: Optional[str]  # 股票全称
    enname: Optional[str]  # 英文全称S深股通
    cnspell: Optional[str]  # 拼音缩写
    market: str  # 市场类型（主板/创业板/科创板/CDR）
    exchange: Optional[str]  # 交易所代码
    curr_type: Optional[str]  # 交易货币
    list_status: Optional[str]  # 上市状态 L上市 D退市 P暂停上市
    list_date: str  # 上市日期
    delist_date: Optional[str]  # 退市日期
    is_hs: Optional[str]  # 是否沪深港通标的，N否 H沪股通 S深股通
    act_name: Optional[str]  # 实控人名称
    act_ent_type: Optional[str]  # 实控人企业性质


# A股日线行情
class AShareDailyParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码（支持多个股票同时提取，逗号分隔）
    trade_date: Optional[str] = None  # 交易日期（YYYYMMDD）
    start_date: Optional[str] = None  # 开始日期(YYYYMMDD)
    end_date: Optional[str] = None  # 结束日期(YYYYMMDD)

class AShareDailyFields(BaseModel):
    ts_code: Optional[str]  # 股票代码
    trade_date: Optional[str]  # 交易日期
    open: Optional[float]  # 开盘价
    high: Optional[float]  # 最高价
    low: Optional[float]  # 最低价
    close: Optional[float]  # 收盘价
    pre_close: Optional[float]  # 昨收价(前复权)
    change: Optional[float]  # 涨跌额
    pct_chg: Optional[float]  # 涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
    vol: Optional[float]  # 成交量 （手）
    amount: Optional[float]  # 成交额 （千元）


# 利润表 https://tushare.pro/document/2?doc_id=33
class IncomeParams(BaseModel):
    ts_code: str  # 股票代码
    ann_date: Optional[str] = None  # 公告日期（YYYYMMDD格式，下同）
    f_ann_date: Optional[str] = None  # 实际公告日期
    start_date: Optional[str] = None  # 公告开始日期
    end_date: Optional[str] = None  # 公告结束日期
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期，比如20171231表示年报)
    report_type: Optional[str] = None  # 报告类型
    comp_type: Optional[str] = None  # 公司类型（1一般工商业2银行3保险4证券）

class IncomeFields(BaseModel):
    ts_code: str  # TS代码
    ann_date: str  # 公告日期
    f_ann_date: str  # 实际公告日期
    end_date: str  # 报告期
    report_type: str  # 报告类型 见底部表
    comp_type: str  # 公司类型(1一般工商业2银行3保险4证券)
    end_type: str  # 报告期类型
    basic_eps: float  # 基本每股收益
    diluted_eps: float  # 稀释每股收益
    total_revenue: float  # 营业总收入
    revenue: float  # 营业收入
    int_income: float  # 利息收入
    prem_earned: float  # 已赚保费
    comm_income: float  # 手续费及佣金收入
    n_commis_income: float  # 手续费及佣金净收入
    n_oth_income: float  # 其他经营净收益
    n_oth_b_income: float  # 加:其他业务净收益
    prem_income: float  # 保险业务收入
    out_prem: float  # 减:分出保费
    une_prem_reser: float  # 提取未到期责任准备金
    reins_income: float  # 其中:分保费收入
    n_sec_tb_income: float  # 代理买卖证券业务净收入
    n_sec_uw_income: float  # 证券承销业务净收入
    n_asset_mg_income: float  # 受托客户资产管理业务净收入
    oth_b_income: float  # 其他业务收入
    fv_value_chg_gain: float  # 加:公允价值变动净收益
    invest_income: float  # 加:投资净收益
    ass_invest_income: float  # 其中:对联营企业和合营企业的投资收益
    forex_gain: float  # 加:汇兑净收益
    total_cogs: float  # 营业总成本
    oper_cost: float  # 减:营业成本
    int_exp: float  # 减:利息支出
    comm_exp: float  # 减:手续费及佣金支出
    biz_tax_surchg: float  # 减:营业税金及附加
    sell_exp: float  # 减:销售费用
    admin_exp: float  # 减:管理费用
    fin_exp: float  # 减:财务费用
    assets_impair_loss: float  # 减:资产减值损失
    prem_refund: float  # 退保金
    compens_payout: float  # 赔付总支出
    reser_insur_liab: float  # 提取保险责任准备金
    div_payt: float  # 保户红利支出
    reins_exp: float  # 分保费用
    oper_exp: float  # 营业支出
    compens_payout_refu: float  # 减:摊回赔付支出
    insur_reser_refu: float  # 减:摊回保险责任准备金
    reins_cost_refund: float  # 减:摊回分保费用
    other_bus_cost: float  # 其他业务成本
    operate_profit: float  # 营业利润
    non_oper_income: float  # 加:营业外收入
    non_oper_exp: float  # 减:营业外支出
    nca_disploss: float  # 其中:减:非流动资产处置净损失
    total_profit: float  # 利润总额
    income_tax: float  # 所得税费用
    n_income: float  # 净利润(含少数股东损益)
    n_income_attr_p: float  # 净利润(不含少数股东损益)
    minority_gain: float  # 少数股东损益
    oth_compr_income: float  # 其他综合收益
    t_compr_income: float  # 综合收益总额
    compr_inc_attr_p: float  # 归属于母公司(或股东)的综合收益总额
    compr_inc_attr_m_s: float  # 归属于少数股东的综合收益总额
    ebit: float  # 息税前利润
    ebitda: float  # 息税折旧摊销前利润
    insurance_exp: float  # 保险业务支出
    undist_profit: float  # 年初未分配利润
    distable_profit: float  # 可分配利润
    rd_exp: float  # 研发费用
    fin_exp_int_exp: float  # 财务费用:利息费用
    fin_exp_int_inc: float  # 财务费用:利息收入
    transfer_surplus_rese: float  # 盈余公积转入
    transfer_housing_imprest: float  # 住房周转金转入
    transfer_oth: float  # 其他转入
    adj_lossgain: float  # 调整以前年度损益
    withdra_legal_surplus: float  # 提取法定盈余公积
    withdra_legal_pubfund: float  # 提取法定公益金
    withdra_biz_devfund: float  # 提取企业发展基金
    withdra_rese_fund: float  # 提取储备基金
    withdra_oth_ersu: float  # 提取任意盈余公积金
    workers_welfare: float  # 职工奖金福利
    distr_profit_shrhder: float  # 可供股东分配的利润
    prfshare_payable_dvd: float  # 应付优先股股利
    comshare_payable_dvd: float  # 应付普通股股利
    capit_comstock_div: float  # 转作股本的普通股股利
    net_after_nr_lp_correct: Optional[float]  # 扣除非经常性损益后的净利润（更正前）
    credit_impa_loss: Optional[float]  # 信用减值损失
    net_expo_hedging_benefits: Optional[float]  # 净敞口套期收益
    oth_impair_loss_assets: Optional[float]  # 其他资产减值损失
    total_opcost: Optional[float]  # 营业总成本（二）
    amodcost_fin_assets: Optional[float]  # 以摊余成本计量的金融资产终止确认收益
    oth_income: Optional[float]  # 其他收益
    asset_disp_income: Optional[float]  # 资产处置收益
    continued_net_profit: Optional[float]  # 持续经营净利润
    end_net_profit: Optional[float]  # 终止经营净利润
    update_flag: str  # 更新标识

# 资产负债表 https://tushare.pro/document/2?doc_id=36
class BalanceSheetParams(BaseModel):
    ts_code: str  # 股票代码
    ann_date: Optional[str] = None  # 公告日期(YYYYMMDD格式，下同)
    start_date: Optional[str] = None  # 公告开始日期
    end_date: Optional[str] = None  # 公告结束日期
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期，比如20171231表示年报)
    report_type: Optional[str] = None  # 报告类型：见下方详细说明
    comp_type: Optional[str] = None  # 公司类型：1一般工商业 2银行 3保险 4证券

class BalanceSheetFields(BaseModel):
    ts_code: str  # TS股票代码
    ann_date: str  # 公告日期
    f_ann_date: str  # 实际公告日期
    end_date: str  # 报告期
    report_type: str  # 报表类型
    comp_type: str  # 公司类型(1一般工商业2银行3保险4证券)
    end_type: str  # 报告期类型
    total_share: float  # 期末总股本
    cap_rese: float  # 资本公积金
    undistr_porfit: float  # 未分配利润
    surplus_rese: float  # 盈余公积金
    special_rese: float  # 专项储备
    money_cap: float  # 货币资金
    trad_asset: float  # 交易性金融资产
    notes_receiv: float  # 应收票据
    accounts_receiv: float  # 应收账款
    oth_receiv: float  # 其他应收款
    prepayment: float  # 预付款项
    div_receiv: float  # 应收股利
    int_receiv: float  # 应收利息
    inventories: float  # 存货
    amor_exp: float  # 待摊费用
    nca_within_1y: float  # 一年内到期的非流动资产
    sett_rsrv: float  # 结算备付金
    loanto_oth_bank_fi: float  # 拆出资金
    premium_receiv: float  # 应收保费
    reinsur_receiv: float  # 应收分保账款
    reinsur_res_receiv: float  # 应收分保合同准备金
    pur_resale_fa: float  # 买入返售金融资产
    oth_cur_assets: float  # 其他流动资产
    total_cur_assets: float  # 流动资产合计
    fa_avail_for_sale: float  # 可供出售金融资产
    htm_invest: float  # 持有至到期投资
    lt_eqt_invest: float  # 长期股权投资
    invest_real_estate: float  # 投资性房地产
    time_deposits: float  # 定期存款
    oth_assets: float  # 其他资产
    lt_rec: float  # 长期应收款
    fix_assets: float  # 固定资产
    cip: float  # 在建工程
    const_materials: float  # 工程物资
    fixed_assets_disp: float  # 固定资产清理
    produc_bio_assets: float  # 生产性生物资产
    oil_and_gas_assets: float  # 油气资产
    intan_assets: float  # 无形资产
    r_and_d: float  # 研发支出
    goodwill: float  # 商誉
    lt_amor_exp: float  # 长期待摊费用
    defer_tax_assets: float  # 递延所得税资产
    decr_in_disbur: float  # 发放贷款及垫款
    oth_nca: float  # 其他非流动资产
    total_nca: float  # 非流动资产合计
    cash_reser_cb: float  # 现金及存放中央银行款项
    depos_in_oth_bfi: float  # 存放同业和其它金融机构款项
    prec_metals: float  # 贵金属
    deriv_assets: float  # 衍生金融资产
    rr_reins_une_prem: float  # 应收分保未到期责任准备金
    rr_reins_outstd_cla: float  # 应收分保未决赔款准备金
    rr_reins_lins_liab: float  # 应收分保寿险责任准备金
    rr_reins_lthins_liab: float  # 应收分保长期健康险责任准备金
    refund_depos: float  # 存出保证金
    ph_pledge_loans: float  # 保户质押贷款
    refund_cap_depos: float  # 存出资本保证金
    indep_acct_assets: float  # 独立账户资产
    client_depos: float  # 其中：客户资金存款
    client_prov: float  # 其中：客户备付金
    transac_seat_fee: float  # 其中:交易席位费
    invest_as_receiv: float  # 应收款项类投资
    total_assets: float  # 资产总计
    lt_borr: float  # 长期借款
    st_borr: float  # 短期借款
    cb_borr: float  # 向中央银行借款
    depos_ib_deposits: float  # 吸收存款及同业存放
    loan_oth_bank: float  # 拆入资金
    trading_fl: float  # 交易性金融负债
    notes_payable: float  # 应付票据
    acct_payable: float  # 应付账款
    adv_receipts: float  # 预收款项
    sold_for_repur_fa: float  # 卖出回购金融资产款
    comm_payable: float  # 应付手续费及佣金
    payroll_payable: float  # 应付职工薪酬
    taxes_payable: float  # 应交税费
    int_payable: float  # 应付利息
    div_payable: float  # 应付股利
    oth_payable: float  # 其他应付款
    acc_exp: float  # 预提费用
    deferred_inc: float  # 递延收益
    st_bonds_payable: float  # 应付短期债券
    payable_to_reinsurer: float  # 应付分保账款
    rsrv_insur_cont: float  # 保险合同准备金
    acting_trading_sec: float  # 代理买卖证券款
    acting_uw_sec: float  # 代理承销证券款
    non_cur_liab_due_1y: float  # 一年内到期的非流动负债
    oth_cur_liab: float  # 其他流动负债
    total_cur_liab: float  # 流动负债合计
    bond_payable: float  # 应付债券
    lt_payable: float  # 长期应付款
    specific_payables: float  # 专项应付款
    estimated_liab: float  # 预计负债
    defer_tax_liab: float  # 递延所得税负债
    defer_inc_non_cur_liab: float  # 递延收益-非流动负债
    oth_ncl: float  # 其他非流动负债
    total_ncl: float  # 非流动负债合计
    depos_oth_bfi: float  # 同业和其它金融机构存放款项
    deriv_liab: float  # 衍生金融负债
    depos: float  # 吸收存款
    agency_bus_liab: float  # 代理业务负债
    oth_liab: float  # 其他负债
    prem_receiv_adva: float  # 预收保费
    depos_received: float  # 存入保证金
    ph_invest: float  # 保户储金及投资款
    reser_une_prem: float  # 未到期责任准备金
    reser_outstd_claims: float  # 未决赔款准备金
    reser_lins_liab: float  # 寿险责任准备金
    reser_lthins_liab: float  # 长期健康险责任准备金
    indept_acc_liab: float  # 独立账户负债
    pledge_borr: float  # 其中:质押借款
    indem_payable: float  # 应付赔付款
    policy_div_payable: float  # 应付保单红利
    total_liab: float  # 负债合计
    treasury_share: float  # 减:库存股
    ordin_risk_reser: float  # 一般风险准备
    forex_differ: float  # 外币报表折算差额
    invest_loss_unconf: float  # 未确认的投资损失
    minority_int: float  # 少数股东权益
    total_hldr_eqy_exc_min_int: float  # 股东权益合计(不含少数股东权益)
    total_hldr_eqy_inc_min_int: float  # 股东权益合计(含少数股东权益)
    total_liab_hldr_eqy: float  # 负债及股东权益总计
    lt_payroll_payable: float  # 长期应付职工薪酬
    oth_comp_income: float  # 其他综合收益
    oth_eqt_tools: float  # 其他权益工具
    oth_eqt_tools_p_shr: float  # 其他权益工具(优先股)
    lending_funds: float  # 融出资金
    acc_receivable: float  # 应收款项
    st_fin_payable: float  # 应付短期融资款
    payables: float  # 应付款项
    hfs_assets: float  # 持有待售的资产
    hfs_sales: float  # 持有待售的负债
    cost_fin_assets: float  # 以摊余成本计量的金融资产
    fair_value_fin_assets: float  # 以公允价值计量且其变动计入其他综合收益的金融资产
    cip_total: float  # 在建工程(合计)(元)
    oth_pay_total: float  # 其他应付款(合计)(元)
    long_pay_total: float  # 长期应付款(合计)(元)
    debt_invest: float  # 债权投资(元)
    oth_debt_invest: float  # 其他债权投资(元)
    oth_eq_invest: Optional[float]  # 其他权益工具投资(元)
    oth_illiq_fin_assets: Optional[float]  # 其他非流动金融资产(元)
    oth_eq_ppbond: Optional[float]  # 其他权益工具:永续债(元)
    receiv_financing: Optional[float]  # 应收款项融资
    use_right_assets: Optional[float]  # 使用权资产
    lease_liab: Optional[float]  # 租赁负债
    contract_assets: float  # 合同资产
    contract_liab: float  # 合同负债
    accounts_receiv_bill: float  # 应收票据及应收账款
    accounts_pay: float  # 应付票据及应付账款
    oth_rcv_total: float  # 其他应收款(合计)（元）
    fix_assets_total: float  # 固定资产(合计)(元)
    update_flag: str  # 更新标识

# 主营业务构成 https://tushare.pro/document/2?doc_id=81
class MainBusinessParams(BaseModel):
    ts_code: str  # 股票代码
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期,比如20171231表示年报)
    type: Optional[str] = None  # 类型：P按产品 D按地区 I按行业（请输入大写字母P或者D）
    start_date: Optional[str] = None  # 报告期开始日期
    end_date: Optional[str] = None  # 报告期结束日期

class MainBusinessFields(BaseModel):
    ts_code: Optional[str]  # TS代码
    end_date: Optional[str]  # 报告期
    bz_item: Optional[str]  # 主营业务来源
    bz_sales: Optional[float]  # 主营业务收入(元)
    bz_profit: Optional[float]  # 主营业务利润(元)
    bz_cost: Optional[float]  # 主营业务成本(元)
    curr_type: Optional[str]  # 货币代码
    update_flag: Optional[str]  # 是否更新
