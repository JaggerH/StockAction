from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

# Define a generic type variable
T = TypeVar('T')

# Define the generic response model
class TushareRequest(GenericModel, Generic[T]):
    params: Optional[T] = None
    fields: List[str]

# Define the generic response model
class TushareResponse(GenericModel, Generic[T]):
    code: int
    msg: Optional[str]
    data: Optional[T]
    
class StockListParams(BaseModel):
    ts_code: Optional[str] = None  # TS股票代码
    name: Optional[str] = None  # 名称
    market: Optional[str] = None  # 市场类别 （主板/创业板/科创板/CDR/北交所）
    list_status: Optional[str] = None  # 上市状态 L上市 D退市 P暂停上市，默认是L
    exchange: Optional[str] = None  # 交易所 SSE上交所 SZSE深交所 BSE北交所
    is_hs: Optional[str] = None  # 是否沪深港通标的，N否 H沪股通 S深股通

StockListRequest = TushareRequest[StockListParams]

class StockListFields(BaseModel):
    ts_code: Optional[str] = None  # TS代码
    symbol: Optional[str] = None  # 股票代码
    name: Optional[str] = None  # 股票名称
    area: Optional[str] = None  # 地域
    industry: Optional[str] = None  # 所属行业
    fullname: Optional[str] = None  # 股票全称
    enname: Optional[str] = None  # 英文全称
    cnspell: Optional[str] = None  # 拼音缩写
    market: Optional[str] = None  # 市场类型（主板/创业板/科创板/CDR）
    exchange: Optional[str] = None  # 交易所代码
    curr_type: Optional[str] = None  # 交易货币
    list_status: Optional[str] = None  # 上市状态 L上市 D退市 P暂停上市
    list_date: Optional[str] = None  # 上市日期
    delist_date: Optional[str] = None  # 退市日期
    is_hs: Optional[str] = None  # 是否沪深港通标的，N否 H沪股通 S深股通
    act_name: Optional[str] = None  # 实控人名称
    act_ent_type: Optional[str] = None  # 实控人企业性质

StockListResponse = TushareResponse[List[StockListFields]]

class AShareDailyParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码（支持多个股票同时提取，逗号分隔）
    trade_date: Optional[str] = None  # 交易日期（YYYYMMDD）
    start_date: Optional[str] = None  # 开始日期(YYYYMMDD)
    end_date: Optional[str] = None  # 结束日期(YYYYMMDD)

AShareDailyRequest = TushareRequest[AShareDailyParams]

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

AShareDailyResponse = TushareResponse[List[AShareDailyFields]]

class IncomeParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码
    ann_date: Optional[str] = None  # 公告日期（YYYYMMDD格式，下同）
    f_ann_date: Optional[str] = None  # 实际公告日期
    start_date: Optional[str] = None  # 公告开始日期
    end_date: Optional[str] = None  # 公告结束日期
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期，比如20171231表示年报)
    report_type: Optional[str] = None  # 报告类型
    comp_type: Optional[str] = None  # 公司类型（1一般工商业2银行3保险4证券）

IncomeRequest = TushareRequest[IncomeParams]

class IncomeFields(BaseModel):
    ts_code: Optional[str] = None  # TS代码
    ann_date: Optional[str] = None  # 公告日期
    f_ann_date: Optional[str] = None  # 实际公告日期
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

IncomeResponse = TushareResponse[List[IncomeFields]]

class BalanceSheetParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码
    ann_date: Optional[str] = None  # 公告日期(YYYYMMDD格式，下同)
    start_date: Optional[str] = None  # 公告开始日期
    end_date: Optional[str] = None  # 公告结束日期
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期，比如20171231表示年报)
    report_type: Optional[str] = None  # 报告类型：见下方详细说明
    comp_type: Optional[str] = None  # 公司类型：1一般工商业 2银行 3保险 4证券

BalanceSheetRequest = TushareRequest[BalanceSheetParams]

class BalanceSheetFields(BaseModel):
    ts_code: Optional[str] = None  # TS股票代码
    ann_date: Optional[str] = None  # 公告日期
    f_ann_date: Optional[str] = None  # 实际公告日期
    end_date: Optional[str] = None  # 报告期
    report_type: Optional[str] = None  # 报表类型
    comp_type: Optional[str] = None  # 公司类型(1一般工商业2银行3保险4证券)
    end_type: Optional[str] = None  # 报告期类型
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
    update_flag: Optional[str] = None  # 更新标识

BalanceSheetResponse = TushareResponse[List[BalanceSheetFields]]

class CashflowParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码
    ann_date: Optional[str] = None  # 公告日期（YYYYMMDD格式，下同）
    f_ann_date: Optional[str] = None  # 实际公告日期
    start_date: Optional[str] = None  # 公告开始日期
    end_date: Optional[str] = None  # 公告结束日期
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期，比如20171231表示年报)
    report_type: Optional[str] = None  # 报告类型：见下方详细说明
    comp_type: Optional[str] = None  # 公司类型：1一般工商业 2银行 3保险 4证券
    is_calc: Optional[int] = None  # 是否计算报表
    start_date: Optional[str] = None  # 公告开始日期
    end_date: Optional[str] = None  # 公告结束日期

CashflowRequest = TushareRequest[CashflowParams]

class CashflowFields(BaseModel):
    ts_code: Optional[str] = None  # TS股票代码
    ann_date: Optional[str] = None  # 公告日期
    f_ann_date: Optional[str] = None  # 实际公告日期
    end_date: Optional[str] = None  # 报告期
    comp_type: Optional[str] = None  # 公司类型(1一般工商业2银行3保险4证券)
    report_type: Optional[str] = None  # 报表类型
    end_type: Optional[str] = None  # 报告期类型
    net_profit: Optional[float] = None  # 净利润
    finan_exp: Optional[float] = None  # 财务费用
    c_fr_sale_sg: Optional[float] = None  # 销售商品、提供劳务收到的现金
    recp_tax_rends: Optional[float] = None  # 收到的税费返还
    n_depos_incr_fi: Optional[float] = None  # 客户存款和同业存放款项净增加额
    n_incr_loans_cb: Optional[float] = None  # 向中央银行借款净增加额
    n_inc_borr_oth_fi: Optional[float] = None  # 向其他金融机构拆入资金净增加额
    prem_fr_orig_contr: Optional[float] = None  # 收到原保险合同保费取得的现金
    n_incr_insured_dep: Optional[float] = None  # 保户储金净增加额
    n_reinsur_prem: Optional[float] = None  # 收到再保业务现金净额
    n_incr_disp_tfa: Optional[float] = None  # 处置交易性金融资产净增加额
    ifc_cash_incr: Optional[float] = None  # 收取利息和手续费净增加额
    n_incr_disp_faas: Optional[float] = None  # 处置可供出售金融资产净增加额
    n_incr_loans_oth_bank: Optional[float] = None  # 拆入资金净增加额
    n_cap_incr_repur: Optional[float] = None  # 回购业务资金净增加额
    c_fr_oth_operate_a: Optional[float] = None  # 收到其他与经营活动有关的现金
    c_inf_fr_operate_a: Optional[float] = None  # 经营活动现金流入小计
    c_paid_goods_s: Optional[float] = None  # 购买商品、接受劳务支付的现金
    c_paid_to_for_empl: Optional[float] = None  # 支付给职工以及为职工支付的现金
    c_paid_for_taxes: Optional[float] = None  # 支付的各项税费
    n_incr_clt_loan_adv: Optional[float] = None  # 客户贷款及垫款净增加额
    n_incr_dep_cbob: Optional[float] = None  # 存放央行和同业款项净增加额
    c_pay_claims_orig_inco: Optional[float] = None  # 支付原保险合同赔付款项的现金
    pay_handling_chrg: Optional[float] = None  # 支付手续费的现金
    pay_comm_insur_plcy: Optional[float] = None  # 支付保单红利的现金
    oth_cash_pay_oper_act: Optional[float] = None  # 支付其他与经营活动有关的现金
    st_cash_out_act: Optional[float] = None  # 经营活动现金流出小计
    n_cashflow_act: Optional[float] = None  # 经营活动产生的现金流量净额
    oth_recp_ral_inv_act: Optional[float] = None  # 收到其他与投资活动有关的现金
    c_disp_withdrwl_invest: Optional[float] = None  # 收回投资收到的现金
    c_recp_return_invest: Optional[float] = None  # 取得投资收益收到的现金
    n_recp_disp_fiolta: Optional[float] = None  # 处置固定资产、无形资产和其他长期资产收回的现金净额
    n_recp_disp_sobu: Optional[float] = None  # 处置子公司及其他营业单位收到的现金净额
    stot_inflows_inv_act: Optional[float] = None  # 投资活动现金流入小计
    c_pay_acq_const_fiolta: Optional[float] = None  # 购建固定资产、无形资产和其他长期资产支付的现金
    c_paid_invest: Optional[float] = None  # 投资支付的现金
    n_disp_subs_oth_biz: Optional[float] = None  # 取得子公司及其他营业单位支付的现金净额
    oth_pay_ral_inv_act: Optional[float] = None  # 支付其他与投资活动有关的现金
    n_incr_pledge_loan: Optional[float] = None  # 质押贷款净增加额
    stot_out_inv_act: Optional[float] = None  # 投资活动现金流出小计
    n_cashflow_inv_act: Optional[float] = None  # 投资活动产生的现金流量净额
    c_recp_borrow: Optional[float] = None  # 取得借款收到的现金
    proc_issue_bonds: Optional[float] = None  # 发行债券收到的现金
    oth_cash_recp_ral_fnc_act: Optional[float] = None  # 收到其他与筹资活动有关的现金
    stot_cash_in_fnc_act: Optional[float] = None  # 筹资活动现金流入小计
    free_cashflow: Optional[float] = None  # 企业自由现金流量
    c_prepay_amt_borr: Optional[float] = None  # 偿还债务支付的现金
    c_pay_dist_dpcp_int_exp: Optional[float] = None  # 分配股利、利润或偿付利息支付的现金
    incl_dvd_profit_paid_sc_ms: Optional[float] = None  # 其中:子公司支付给少数股东的股利、利润
    oth_cashpay_ral_fnc_act: Optional[float] = None  # 支付其他与筹资活动有关的现金
    stot_cashout_fnc_act: Optional[float] = None  # 筹资活动现金流出小计
    n_cash_flows_fnc_act: Optional[float] = None  # 筹资活动产生的现金流量净额
    eff_fx_flu_cash: Optional[float] = None  # 汇率变动对现金的影响
    n_incr_cash_cash_equ: Optional[float] = None  # 现金及现金等价物净增加额
    c_cash_equ_beg_period: Optional[float] = None  # 期初现金及现金等价物余额
    c_cash_equ_end_period: Optional[float] = None  # 期末现金及现金等价物余额
    c_recp_cap_contrib: Optional[float] = None  # 吸收投资收到的现金
    incl_cash_rec_saims: Optional[float] = None  # 其中:子公司吸收少数股东投资收到的现金
    uncon_invest_loss: Optional[float] = None  # 未确认投资损失
    prov_depr_assets: Optional[float] = None  # 加:资产减值准备
    depr_fa_coga_dpba: Optional[float] = None  # 固定资产折旧、油气资产折耗、生产性生物资产折旧
    amort_intang_assets: Optional[float] = None  # 无形资产摊销
    lt_amort_deferred_exp: Optional[float] = None  # 长期待摊费用摊销
    decr_deferred_exp: Optional[float] = None  # 待摊费用减少
    incr_acc_exp: Optional[float] = None  # 预提费用增加
    loss_disp_fiolta: Optional[float] = None  # 处置固定、无形资产和其他长期资产的损失
    loss_scr_fa: Optional[float] = None  # 固定资产报废损失
    loss_fv_chg: Optional[float] = None  # 公允价值变动损失
    invest_loss: Optional[float] = None  # 投资损失
    decr_def_inc_tax_assets: Optional[float] = None  # 递延所得税资产减少
    incr_def_inc_tax_liab: Optional[float] = None  # 递延所得税负债增加
    decr_inventories: Optional[float] = None  # 存货的减少
    decr_oper_payable: Optional[float] = None  # 经营性应收项目的减少
    incr_oper_payable: Optional[float] = None  # 经营性应付项目的增加
    others: Optional[float] = None  # 其他
    im_net_cashflow_oper_act: Optional[float] = None  # 经营活动产生的现金流量净额(间接法)
    conv_debt_into_cap: Optional[float] = None  # 债务转为资本
    conv_copbonds_due_within_1y: Optional[float] = None  # 一年内到期的可转换公司债券
    fa_fnc_leases: Optional[float] = None  # 融资租入固定资产
    im_n_incr_cash_equ: Optional[float] = None  # 现金及现金等价物净增加额(间接法)
    net_dism_capital_add: Optional[float] = None  # 拆出资金净增加额
    net_cash_rece_sec: Optional[float] = None  # 代理买卖证券收到的现金净额(元)
    credit_impa_loss: Optional[float] = None  # 信用减值损失
    use_right_asset_dep: Optional[float] = None  # 使用权资产折旧
    oth_loss_asset: Optional[float] = None  # 其他资产减值损失
    end_bal_cash: Optional[float] = None  # 现金的期末余额
    beg_bal_cash: Optional[float] = None  # 减:现金的期初余额
    end_bal_cash_equ: Optional[float] = None  # 加:现金等价物的期末余额
    beg_bal_cash_equ: Optional[float] = None  # 减:现金等价物的期初余额
    update_flag: Optional[str] = None  # 更新标志(1最新）

CashflowResponse = TushareResponse[List[CashflowFields]]

class MainBusinessParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码
    period: Optional[str] = None  # 报告期(每个季度最后一天的日期,比如20171231表示年报)
    type: Optional[str] = None  # 类型：P按产品 D按地区 I按行业（请输入大写字母P或者D）
    start_date: Optional[str] = None  # 报告期开始日期
    end_date: Optional[str] = None  # 报告期结束日期

MainBusinessRequest = TushareRequest[MainBusinessParams]

class MainBusinessFields(BaseModel):
    ts_code: Optional[str] = None  # TS代码
    end_date: Optional[str] = None  # 报告期
    bz_item: Optional[str] = None  # 主营业务来源
    bz_sales: Optional[float] = None  # 主营业务收入(元)
    bz_profit: Optional[float] = None  # 主营业务利润(元)
    bz_cost: Optional[float] = None  # 主营业务成本(元)
    curr_type: Optional[str] = None  # 货币代码
    update_flag: Optional[str] = None  # 是否更新

MainBusinessResponse = TushareResponse[List[MainBusinessFields]]

class ConceptParams(BaseModel):
    src: Optional[str] = None  # 来源，默认为ts

ConceptRequest = TushareRequest[ConceptParams]

class ConceptFields(BaseModel):
    code: Optional[str] = None  # 概念分类ID
    name: Optional[str] = None  # 概念分类名称
    src: Optional[str] = None  # 来源

ConceptResponse = TushareResponse[List[ConceptFields]]

class LimitListParams(BaseModel):
    trade_date: Optional[str] = None  # 交易日期
    ts_code: Optional[str] = None  # 股票代码
    limit_type: Optional[str] = None  # 涨跌停类型（U涨停D跌停Z炸板）
    exchange: Optional[str] = None  # 交易所（SH上交所SZ深交所BJ北交所）
    start_date: Optional[str] = None  # 开始日期
    end_date: Optional[str] = None  # 结束日期

LimitListRequest = TushareRequest[LimitListParams]

class LimitListFields(BaseModel):
    trade_date: Optional[str] = None  # 交易日期
    ts_code: Optional[str] = None  # 股票代码
    industry: Optional[str] = None  # 所属行业
    name: Optional[str] = None  # 股票名称
    close: Optional[float] = None  # 收盘价
    pct_chg: Optional[float] = None  # 涨跌幅
    amount: Optional[float] = None  # 成交额
    limit_amount: Optional[float] = None  # 板上成交金额(涨停无此数据)
    float_mv: Optional[float] = None  # 流通市值
    total_mv: Optional[float] = None  # 总市值
    turnover_ratio: Optional[float] = None  # 换手率
    fd_amount: Optional[float] = None  # 封单金额
    first_time: Optional[str] = None  # 首次封板时间（跌停无此数据）
    last_time: Optional[str] = None  # 最后封板时间
    open_times: Optional[int] = None  # 炸板次数(跌停为开板次数)
    up_stat: Optional[str] = None  # 涨停统计（N/T T天有N次涨停）
    limit_times: Optional[int] = None  # 连板数
    limit: Optional[str] = None  # D跌停U涨停Z炸板

LimitListResponse = TushareResponse[List[LimitListFields]]

class DailyBasicParams(BaseModel):
    ts_code: Optional[str] = None  # 股票代码（二选一）
    trade_date: Optional[str] = None  # 交易日期 （二选一）
    start_date: Optional[str] = None  # 开始日期(YYYYMMDD)
    end_date: Optional[str] = None  # 结束日期(YYYYMMDD)

DailyBasicRequest = TushareRequest[DailyBasicParams]

class DailyBasicFields(BaseModel):
    ts_code: Optional[str] = None  # TS股票代码
    trade_date: Optional[str] = None  # 交易日期
    close: Optional[float] = None  # 当日收盘价
    turnover_rate: Optional[float] = None  # 换手率（%）
    turnover_rate_f: Optional[float] = None  # 换手率（自由流通股）
    volume_ratio: Optional[float] = None  # 量比
    pe: Optional[float] = None  # 市盈率（总市值/净利润， 亏损的PE为空）
    pe_ttm: Optional[float] = None  # 市盈率（TTM，亏损的PE为空）
    pb: Optional[float] = None  # 市净率（总市值/净资产）
    ps: Optional[float] = None  # 市销率
    ps_ttm: Optional[float] = None  # 市销率（TTM）
    dv_ratio: Optional[float] = None  # 股息率 （%）
    dv_ttm: Optional[float] = None  # 股息率（TTM）（%）
    total_share: Optional[float] = None  # 总股本 （万股）
    float_share: Optional[float] = None  # 流通股本 （万股）
    free_share: Optional[float] = None  # 自由流通股本 （万）
    total_mv: Optional[float] = None  # 总市值 （万元）
    circ_mv: Optional[float] = None  # 流通市值（万元）

DailyBasicResponse = TushareResponse[List[DailyBasicFields]]

class IndexMemberParams(BaseModel):
    index_code: Optional[str] = None  # 指数代码
    ts_code: Optional[str] = None  # 股票代码
    is_new: Optional[str] = None  # 是否最新（默认为“Y是”）

IndexMemberRequest = TushareRequest[IndexMemberParams]

class IndexMemberFields(BaseModel):
    index_code: Optional[str] = None  # 指数代码
    index_name: Optional[str] = None  # 指数名称
    con_code: Optional[str] = None  # 成分股票代码
    con_name: Optional[str] = None  # 成分股票名称
    in_date: Optional[str] = None  # 纳入日期
    out_date: Optional[str] = None  # 剔除日期
    is_new: Optional[str] = None  # 是否最新Y是N否

IndexMemberResponse = TushareResponse[List[IndexMemberFields]]

class DailyInfoParams(BaseModel):
    trade_date: Optional[str] = None  # 交易日期（YYYYMMDD格式，下同）
    ts_code: Optional[str] = None  # 板块代码（请参阅下方列表）
    exchange: Optional[str] = None  # 股票市场（SH上交所 SZ深交所）
    start_date: Optional[str] = None  # 开始日期
    end_date: Optional[str] = None  # 结束日期
    fields: Optional[str] = None  # 指定提取字段

DailyInfoRequest = TushareRequest[DailyInfoParams]

class DailyInfoFields(BaseModel):
    trade_date: Optional[str] = None  # 交易日期
    ts_code: Optional[str] = None  # 市场代码
    ts_name: Optional[str] = None  # 市场名称
    com_count: Optional[int] = None  # 挂牌数
    total_share: Optional[float] = None  # 总股本（亿股）
    float_share: Optional[float] = None  # 流通股本（亿股）
    total_mv: Optional[float] = None  # 总市值（亿元）
    float_mv: Optional[float] = None  # 流通市值（亿元）
    amount: Optional[float] = None  # 交易金额（亿元）
    vol: Optional[float] = None  # 成交量（亿股）
    trans_count: Optional[int] = None  # 成交笔数（万笔）
    pe: Optional[float] = None  # 平均市盈率
    tr: Optional[float] = None  # 换手率（％），注：深交所暂无此列
    exchange: Optional[str] = None  # 交易所（SH上交所 SZ深交所）

DailyInfoResponse = TushareResponse[List[DailyInfoFields]]

class ThsIndexParams(BaseModel):
    ts_code: Optional[str] = None  # 指数代码
    exchange: Optional[str] = None  # 市场类型A-a股 HK-港股 US-美股
    type: Optional[str] = None  # 指数类型 N-板块指数 I-行业指数 R-地域指数 S-同花顺特色指数

ThsIndexRequest = TushareRequest[ThsIndexParams]

class ThsIndexFields(BaseModel):
    ts_code: Optional[str] = None  # 代码
    name: Optional[str] = None  # 名称
    count: Optional[int] = None  # 成分个数
    exchange: Optional[str] = None  # 交易所
    list_date: Optional[str] = None  # 上市日期
    type: Optional[str] = None  # N概念指数S特色指数

ThsIndexResponse = TushareResponse[List[ThsIndexFields]]

class ThsDailyParams(BaseModel):
    ts_code: Optional[str] = None  # 指数代码
    trade_date: Optional[str] = None  # 交易日期（YYYYMMDD格式，下同）
    start_date: Optional[str] = None  # 开始日期
    end_date: Optional[str] = None  # 结束日期

ThsDailyRequest = TushareRequest[ThsDailyParams]

class ThsDailyFields(BaseModel):
    ts_code: Optional[str] = None  # TS指数代码
    trade_date: Optional[str] = None  # 交易日
    close: Optional[float] = None  # 收盘点位
    open: Optional[float] = None  # 开盘点位
    high: Optional[float] = None  # 最高点位
    low: Optional[float] = None  # 最低点位
    pre_close: Optional[float] = None  # 昨日收盘点
    avg_price: Optional[float] = None  # 平均价
    change: Optional[float] = None  # 涨跌点位
    pct_change: Optional[float] = None  # 涨跌幅
    vol: Optional[float] = None  # 成交量
    turnover_rate: Optional[float] = None  # 换手率
    total_mv: Optional[float] = None  # 总市值
    float_mv: Optional[float] = None  # 流通市值

ThsDailyResponse = TushareResponse[List[ThsDailyFields]]

class ThsMemberParams(BaseModel):
    ts_code: Optional[str] = None  # 板块指数代码
    code: Optional[str] = None  # 股票代码

ThsMemberRequest = TushareRequest[ThsMemberParams]

class ThsMemberFields(BaseModel):
    ts_code: Optional[str] = None  # 指数代码
    code: Optional[str] = None  # 股票代码
    name: Optional[str] = None  # 股票名称
    weight: Optional[float] = None  # 权重(暂无)
    in_date: Optional[str] = None  # 纳入日期(暂无)
    out_date: Optional[str] = None  # 剔除日期(暂无)
    is_new: Optional[str] = None  # 是否最新Y是N否

ThsMemberResponse = TushareResponse[List[ThsMemberFields]]

