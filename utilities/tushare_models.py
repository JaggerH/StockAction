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
    fullname: Optional[str] = None  # 股票全称
    enname: Optional[str] = None  # 英文全称S深股通
    cnspell: Optional[str] = None  # 拼音缩写
    market: Optional[str] = None  # 市场类型（主板/创业板/科创板/CDR）
    exchange: Optional[str] = None  # 交易所代码
    curr_type: Optional[str] = None  # 交易货币
    list_status: Optional[str] = None  # 上市状态 L上市 D退市 P暂停上市
    list_date: str  # 上市日期
    delist_date: Optional[str] = None  # 退市日期
    is_hs: Optional[str] = None  # 是否沪深港通标的，N否 H沪股通 S深股通
    act_name: Optional[str] = None  # 实控人名称
    act_ent_type: Optional[str] = None  # 实控人企业性质


# A股日线行情
class AShareDailyParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码（支持多个股票同时提取，逗号分隔）
    trade_date: Optional[str] = None  # 交易日期（YYYYMMDD）
    start_date: Optional[str] = None  # 开始日期(YYYYMMDD)
    end_date: Optional[str] = None  # 结束日期(YYYYMMDD)

class AShareDailyFields(BaseModel):
    ts_code: Optional[str] = None  # 股票代码
    trade_date: Optional[str] = None  # 交易日期
    open: Optional[float] = None  # 开盘价
    high: Optional[float] = None  # 最高价
    low: Optional[float] = None  # 最低价
    close: Optional[float] = None  # 收盘价
    pre_close: Optional[float] = None  # 昨收价(前复权)
    change: Optional[float] = None  # 涨跌额
    pct_chg: Optional[float] = None  # 涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
    vol: Optional[float] = None  # 成交量 （手）
    amount: Optional[float] = None  # 成交额 （千元）


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
    ts_code: Optional[str] = None  # TS代码
    ann_date: Optional[str] = None  # 公告日期
    f_ann_date: Optional[str] = None   # 实际公告日期
    end_date: Optional[str] = None  # 报告期
    report_type: Optional[str] = None  # 报告类型 见底部表
    comp_type: Optional[str] = None  # 公司类型(1一般工商业2银行3保险4证券)
    end_type: Optional[str] = None  # 报告期类型
    basic_eps: Optional[float] = None  # 基本每股收益
    diluted_eps: Optional[float] = None  # 稀释每股收益
    total_revenue: Optional[float] = None  # 营业总收入
    revenue: Optional[float] = None  # 营业收入
    int_income: Optional[float] = None  # 利息收入
    prem_earned: Optional[float] = None  # 已赚保费
    comm_income: Optional[float] = None  # 手续费及佣金收入
    n_commis_income: Optional[float] = None  # 手续费及佣金净收入
    n_oth_income: Optional[float] = None  # 其他经营净收益
    n_oth_b_income: Optional[float] = None  # 加:其他业务净收益
    prem_income: Optional[float] = None  # 保险业务收入
    out_prem: Optional[float] = None  # 减:分出保费
    une_prem_reser: Optional[float] = None  # 提取未到期责任准备金
    reins_income: Optional[float] = None  # 其中:分保费收入
    n_sec_tb_income: Optional[float] = None  # 代理买卖证券业务净收入
    n_sec_uw_income: Optional[float] = None  # 证券承销业务净收入
    n_asset_mg_income: Optional[float] = None  # 受托客户资产管理业务净收入
    oth_b_income: Optional[float] = None  # 其他业务收入
    fv_value_chg_gain: Optional[float] = None  # 加:公允价值变动净收益
    invest_income: Optional[float] = None  # 加:投资净收益
    ass_invest_income: Optional[float] = None  # 其中:对联营企业和合营企业的投资收益
    forex_gain: Optional[float] = None  # 加:汇兑净收益
    total_cogs: Optional[float] = None  # 营业总成本
    oper_cost: Optional[float] = None  # 减:营业成本
    int_exp: Optional[float] = None  # 减:利息支出
    comm_exp: Optional[float] = None  # 减:手续费及佣金支出
    biz_tax_surchg: Optional[float] = None  # 减:营业税金及附加
    sell_exp: Optional[float] = None  # 减:销售费用
    admin_exp: Optional[float] = None  # 减:管理费用
    fin_exp: Optional[float] = None  # 减:财务费用
    assets_impair_loss: Optional[float] = None  # 减:资产减值损失
    prem_refund: Optional[float] = None  # 退保金
    compens_payout: Optional[float] = None  # 赔付总支出
    reser_insur_liab: Optional[float] = None  # 提取保险责任准备金
    div_payt: Optional[float] = None  # 保户红利支出
    reins_exp: Optional[float] = None  # 分保费用
    oper_exp: Optional[float] = None  # 营业支出
    compens_payout_refu: Optional[float] = None  # 减:摊回赔付支出
    insur_reser_refu: Optional[float] = None  # 减:摊回保险责任准备金
    reins_cost_refund: Optional[float] = None  # 减:摊回分保费用
    other_bus_cost: Optional[float] = None  # 其他业务成本
    operate_profit: Optional[float] = None  # 营业利润
    non_oper_income: Optional[float] = None  # 加:营业外收入
    non_oper_exp: Optional[float] = None  # 减:营业外支出
    nca_disploss: Optional[float] = None  # 其中:减:非流动资产处置净损失
    total_profit: Optional[float] = None  # 利润总额
    income_tax: Optional[float] = None  # 所得税费用
    n_income: Optional[float] = None  # 净利润(含少数股东损益)
    n_income_attr_p: Optional[float] = None  # 净利润(不含少数股东损益)
    minority_gain: Optional[float] = None  # 少数股东损益
    oth_compr_income: Optional[float] = None  # 其他综合收益
    t_compr_income: Optional[float] = None  # 综合收益总额
    compr_inc_attr_p: Optional[float] = None  # 归属于母公司(或股东)的综合收益总额
    compr_inc_attr_m_s: Optional[float] = None  # 归属于少数股东的综合收益总额
    ebit: Optional[float] = None  # 息税前利润
    ebitda: Optional[float] = None  # 息税折旧摊销前利润
    insurance_exp: Optional[float] = None  # 保险业务支出
    undist_profit: Optional[float] = None  # 年初未分配利润
    distable_profit: Optional[float] = None  # 可分配利润
    rd_exp: Optional[float] = None  # 研发费用
    fin_exp_int_exp: Optional[float] = None  # 财务费用:利息费用
    fin_exp_int_inc: Optional[float] = None  # 财务费用:利息收入
    transfer_surplus_rese: Optional[float] = None  # 盈余公积转入
    transfer_housing_imprest: Optional[float] = None  # 住房周转金转入
    transfer_oth: Optional[float] = None  # 其他转入
    adj_lossgain: Optional[float] = None  # 调整以前年度损益
    withdra_legal_surplus: Optional[float] = None  # 提取法定盈余公积
    withdra_legal_pubfund: Optional[float] = None  # 提取法定公益金
    withdra_biz_devfund: Optional[float] = None  # 提取企业发展基金
    withdra_rese_fund: Optional[float] = None  # 提取储备基金
    withdra_oth_ersu: Optional[float] = None  # 提取任意盈余公积金
    workers_welfare: Optional[float] = None  # 职工奖金福利
    distr_profit_shrhder: Optional[float] = None  # 可供股东分配的利润
    prfshare_payable_dvd: Optional[float] = None  # 应付优先股股利
    comshare_payable_dvd: Optional[float] = None  # 应付普通股股利
    capit_comstock_div: Optional[float] = None  # 转作股本的普通股股利
    net_after_nr_lp_correct: Optional[float] = None  # 扣除非经常性损益后的净利润（更正前）
    credit_impa_loss: Optional[float] = None  # 信用减值损失
    net_expo_hedging_benefits: Optional[float] = None  # 净敞口套期收益
    oth_impair_loss_assets: Optional[float] = None  # 其他资产减值损失
    total_opcost: Optional[float] = None  # 营业总成本（二）
    amodcost_fin_assets: Optional[float] = None  # 以摊余成本计量的金融资产终止确认收益
    oth_income: Optional[float] = None  # 其他收益
    asset_disp_income: Optional[float] = None  # 资产处置收益
    continued_net_profit: Optional[float] = None  # 持续经营净利润
    end_net_profit: Optional[float] = None  # 终止经营净利润
    update_flag: Optional[str] = None  # 更新标识

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
    ts_code: Optional[str] = None # TS股票代码
    ann_date: Optional[str] = None # 公告日期
    f_ann_date: Optional[str] = None # 实际公告日期
    end_date: Optional[str] = None # 报告期
    report_type: Optional[str] = None # 报表类型
    comp_type: Optional[str] = None # 公司类型(1一般工商业2银行3保险4证券)
    end_type: Optional[str] = None # 报告期类型
    total_share: Optional[float] = None  # 期末总股本
    cap_rese: Optional[float] = None  # 资本公积金
    undistr_porfit: Optional[float] = None  # 未分配利润
    surplus_rese: Optional[float] = None  # 盈余公积金
    special_rese: Optional[float] = None  # 专项储备
    money_cap: Optional[float] = None  # 货币资金
    trad_asset: Optional[float] = None  # 交易性金融资产
    notes_receiv: Optional[float] = None  # 应收票据
    accounts_receiv: Optional[float] = None  # 应收账款
    oth_receiv: Optional[float] = None  # 其他应收款
    prepayment: Optional[float] = None  # 预付款项
    div_receiv: Optional[float] = None  # 应收股利
    int_receiv: Optional[float] = None  # 应收利息
    inventories: Optional[float] = None  # 存货
    amor_exp: Optional[float] = None  # 待摊费用
    nca_within_1y: Optional[float] = None  # 一年内到期的非流动资产
    sett_rsrv: Optional[float] = None  # 结算备付金
    loanto_oth_bank_fi: Optional[float] = None  # 拆出资金
    premium_receiv: Optional[float] = None  # 应收保费
    reinsur_receiv: Optional[float] = None  # 应收分保账款
    reinsur_res_receiv: Optional[float] = None  # 应收分保合同准备金
    pur_resale_fa: Optional[float] = None  # 买入返售金融资产
    oth_cur_assets: Optional[float] = None  # 其他流动资产
    total_cur_assets: Optional[float] = None  # 流动资产合计
    fa_avail_for_sale: Optional[float] = None  # 可供出售金融资产
    htm_invest: Optional[float] = None  # 持有至到期投资
    lt_eqt_invest: Optional[float] = None  # 长期股权投资
    invest_real_estate: Optional[float] = None  # 投资性房地产
    time_deposits: Optional[float] = None  # 定期存款
    oth_assets: Optional[float] = None  # 其他资产
    lt_rec: Optional[float] = None  # 长期应收款
    fix_assets: Optional[float] = None  # 固定资产
    cip: Optional[float] = None  # 在建工程
    const_materials: Optional[float] = None  # 工程物资
    fixed_assets_disp: Optional[float] = None  # 固定资产清理
    produc_bio_assets: Optional[float] = None  # 生产性生物资产
    oil_and_gas_assets: Optional[float] = None  # 油气资产
    intan_assets: Optional[float] = None  # 无形资产
    r_and_d: Optional[float] = None  # 研发支出
    goodwill: Optional[float] = None  # 商誉
    lt_amor_exp: Optional[float] = None  # 长期待摊费用
    defer_tax_assets: Optional[float] = None  # 递延所得税资产
    decr_in_disbur: Optional[float] = None  # 发放贷款及垫款
    oth_nca: Optional[float] = None  # 其他非流动资产
    total_nca: Optional[float] = None  # 非流动资产合计
    cash_reser_cb: Optional[float] = None  # 现金及存放中央银行款项
    depos_in_oth_bfi: Optional[float] = None  # 存放同业和其它金融机构款项
    prec_metals: Optional[float] = None  # 贵金属
    deriv_assets: Optional[float] = None  # 衍生金融资产
    rr_reins_une_prem: Optional[float] = None  # 应收分保未到期责任准备金
    rr_reins_outstd_cla: Optional[float] = None  # 应收分保未决赔款准备金
    rr_reins_lins_liab: Optional[float] = None  # 应收分保寿险责任准备金
    rr_reins_lthins_liab: Optional[float] = None  # 应收分保长期健康险责任准备金
    refund_depos: Optional[float] = None  # 存出保证金
    ph_pledge_loans: Optional[float] = None  # 保户质押贷款
    refund_cap_depos: Optional[float] = None  # 存出资本保证金
    indep_acct_assets: Optional[float] = None  # 独立账户资产
    client_depos: Optional[float] = None  # 其中：客户资金存款
    client_prov: Optional[float] = None  # 其中：客户备付金
    transac_seat_fee: Optional[float] = None  # 其中:交易席位费
    invest_as_receiv: Optional[float] = None  # 应收款项类投资
    total_assets: Optional[float] = None  # 资产总计
    lt_borr: Optional[float] = None  # 长期借款
    st_borr: Optional[float] = None  # 短期借款
    cb_borr: Optional[float] = None  # 向中央银行借款
    depos_ib_deposits: Optional[float] = None  # 吸收存款及同业存放
    loan_oth_bank: Optional[float] = None  # 拆入资金
    trading_fl: Optional[float] = None  # 交易性金融负债
    notes_payable: Optional[float] = None  # 应付票据
    acct_payable: Optional[float] = None  # 应付账款
    adv_receipts: Optional[float] = None  # 预收款项
    sold_for_repur_fa: Optional[float] = None  # 卖出回购金融资产款
    comm_payable: Optional[float] = None  # 应付手续费及佣金
    payroll_payable: Optional[float] = None  # 应付职工薪酬
    taxes_payable: Optional[float] = None  # 应交税费
    int_payable: Optional[float] = None  # 应付利息
    div_payable: Optional[float] = None  # 应付股利
    oth_payable: Optional[float] = None  # 其他应付款
    acc_exp: Optional[float] = None  # 预提费用
    deferred_inc: Optional[float] = None  # 递延收益
    st_bonds_payable: Optional[float] = None  # 应付短期债券
    payable_to_reinsurer: Optional[float] = None  # 应付分保账款
    rsrv_insur_cont: Optional[float] = None  # 保险合同准备金
    acting_trading_sec: Optional[float] = None  # 代理买卖证券款
    acting_uw_sec: Optional[float] = None  # 代理承销证券款
    non_cur_liab_due_1y: Optional[float] = None  # 一年内到期的非流动负债
    oth_cur_liab: Optional[float] = None  # 其他流动负债
    total_cur_liab: Optional[float] = None  # 流动负债合计
    bond_payable: Optional[float] = None  # 应付债券
    lt_payable: Optional[float] = None  # 长期应付款
    specific_payables: Optional[float] = None  # 专项应付款
    estimated_liab: Optional[float] = None  # 预计负债
    defer_tax_liab: Optional[float] = None  # 递延所得税负债
    defer_inc_non_cur_liab: Optional[float] = None  # 递延收益-非流动负债
    oth_ncl: Optional[float] = None  # 其他非流动负债
    total_ncl: Optional[float] = None  # 非流动负债合计
    depos_oth_bfi: Optional[float] = None  # 同业和其它金融机构存放款项
    deriv_liab: Optional[float] = None  # 衍生金融负债
    depos: Optional[float] = None  # 吸收存款
    agency_bus_liab: Optional[float] = None  # 代理业务负债
    oth_liab: Optional[float] = None  # 其他负债
    prem_receiv_adva: Optional[float] = None  # 预收保费
    depos_received: Optional[float] = None  # 存入保证金
    ph_invest: Optional[float] = None  # 保户储金及投资款
    reser_une_prem: Optional[float] = None  # 未到期责任准备金
    reser_outstd_claims: Optional[float] = None  # 未决赔款准备金
    reser_lins_liab: Optional[float] = None  # 寿险责任准备金
    reser_lthins_liab: Optional[float] = None  # 长期健康险责任准备金
    indept_acc_liab: Optional[float] = None  # 独立账户负债
    pledge_borr: Optional[float] = None  # 其中:质押借款
    indem_payable: Optional[float] = None  # 应付赔付款
    policy_div_payable: Optional[float] = None  # 应付保单红利
    total_liab: Optional[float] = None  # 负债合计
    treasury_share: Optional[float] = None  # 减:库存股
    ordin_risk_reser: Optional[float] = None  # 一般风险准备
    forex_differ: Optional[float] = None  # 外币报表折算差额
    invest_loss_unconf: Optional[float] = None  # 未确认的投资损失
    minority_int: Optional[float] = None  # 少数股东权益
    total_hldr_eqy_exc_min_int: Optional[float] = None  # 股东权益合计(不含少数股东权益)
    total_hldr_eqy_inc_min_int: Optional[float] = None  # 股东权益合计(含少数股东权益)
    total_liab_hldr_eqy: Optional[float] = None  # 负债及股东权益总计
    lt_payroll_payable: Optional[float] = None  # 长期应付职工薪酬
    oth_comp_income: Optional[float] = None  # 其他综合收益
    oth_eqt_tools: Optional[float] = None  # 其他权益工具
    oth_eqt_tools_p_shr: Optional[float] = None  # 其他权益工具(优先股)
    lending_funds: Optional[float] = None  # 融出资金
    acc_receivable: Optional[float] = None  # 应收款项
    st_fin_payable: Optional[float] = None  # 应付短期融资款
    payables: Optional[float] = None  # 应付款项
    hfs_assets: Optional[float] = None  # 持有待售的资产
    hfs_sales: Optional[float] = None  # 持有待售的负债
    cost_fin_assets: Optional[float] = None  # 以摊余成本计量的金融资产
    fair_value_fin_assets: Optional[float] = None  # 以公允价值计量且其变动计入其他综合收益的金融资产
    cip_total: Optional[float] = None  # 在建工程(合计)(元)
    oth_pay_total: Optional[float] = None  # 其他应付款(合计)(元)
    long_pay_total: Optional[float] = None  # 长期应付款(合计)(元)
    debt_invest: Optional[float] = None  # 债权投资(元)
    oth_debt_invest: Optional[float] = None  # 其他债权投资(元)
    oth_eq_invest: Optional[float] = None  # 其他权益工具投资(元)
    oth_illiq_fin_assets: Optional[float] = None  # 其他非流动金融资产(元)
    oth_eq_ppbond: Optional[float] = None  # 其他权益工具:永续债(元)
    receiv_financing: Optional[float] = None  # 应收款项融资
    use_right_assets: Optional[float] = None  # 使用权资产
    lease_liab: Optional[float] = None  # 租赁负债
    contract_assets: Optional[float] = None  # 合同资产
    contract_liab: Optional[float] = None  # 合同负债
    accounts_receiv_bill: Optional[float] = None  # 应收票据及应收账款
    accounts_pay: Optional[float] = None  # 应付票据及应付账款
    oth_rcv_total: Optional[float] = None  # 其他应收款(合计)（元）
    fix_assets_total: Optional[float] = None  # 固定资产(合计)(元)
    update_flag: Optional[str] = None # 更新标识

# 主营业务构成 https://tushare.pro/document/2?doc_id=81
class MainBusinessParams(BaseModel):
    ts_code: str  # 股票代码
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期,比如20171231表示年报)
    type: Optional[str] = None  # 类型：P按产品 D按地区 I按行业（请输入大写字母P或者D）
    start_date: Optional[str] = None  # 报告期开始日期
    end_date: Optional[str] = None  # 报告期结束日期

class MainBusinessFields(BaseModel):
    ts_code: Optional[str] = None  # TS代码
    end_date: Optional[str] = None  # 报告期
    bz_item: Optional[str] = None  # 主营业务来源
    bz_sales: Optional[float] = None  # 主营业务收入(元)
    bz_profit: Optional[float] = None  # 主营业务利润(元)
    bz_cost: Optional[float] = None  # 主营业务成本(元)
    curr_type: Optional[str] = None  # 货币代码
    update_flag: Optional[str] = None  # 是否更新
