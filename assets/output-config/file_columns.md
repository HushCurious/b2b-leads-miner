# Default Output Field Dictionary

Use this file as the default field-definition document for exported lead files.

If `file_columns_userDefine.md` contains a customized version, use the user-defined file instead.

## How To Use

- This file defines what each field means.
- It can also record suggested values or controlled vocabularies.
- Keep adding to this file as sales clarifies the schema.
- If a later user wants a different structure, copy and modify the content in `file_columns_userDefine.md`.

## Fields

| Field | Description | Suggested Values / Fill Rules |
| --- | --- | --- |
| Region | 市场区域。用于标记该公司主要对应的销售市场区域，不是注册地。 | 例如填写 `欧洲`、`亚洲`、`中东`、`东南亚` 等。 |
| Country | 公司所在国家，或网页/资料中显示的主要国家。 | 直接填写国家名称，如 `Turkey`、`Israel`、`Spain`、`China`。 |
| CompanyName | 主公司名、品牌名或跟进主体名称。 | 直接填写公司官方名称或常用商业名称。 |
| Channel | 该公司在销售链路中的商业角色，用于判断它更接近生产商、总代、分销商、经销商，还是零售门店类渠道。判断时可参考官网里的品牌关系、授权信息、dealer/distributor/network 页面，以及是否自有品牌生产。 | 默认分类：`A: manufacturer`、`B1: master distributor`、`B2: distributor`、`B3: dealer`、`C1: online store`、`C2: chain store`、`C3: pop store`。输出时该字段只写代码：`A`、`B1`、`B2`、`B3`、`C1`、`C2`、`C3`，不写中文或英文说明；代码说明放在结果文件末尾。 |
| Specialty | 与目标泳池分销客户画像的匹配等级。用于判断这家公司和目标泳池分销客户画像的接近程度。 | 输出值可用 `1` 到 `5`。`1` = 匹配度低，泳池业务占比低于 50%，或主营方向明显不在泳池分销；`2` = 有泳池相关业务，但主要是设计、安装或维护，不以分销或进口为核心；`3` = 有泳池业务，但跨行产品较多，且非泳池业务权重在 50% 或更高；`4` = 有泳池业务，也有跨行产品，但非泳池业务权重低于 50%；`5` = 高匹配，100% 专注泳池设备分销或进口，且分销产品齐全，没有跨行产品。输出时该字段只写 `1` 到 `5` 的等级值，不写中文或英文说明；信息不足时留空。 |
| Scale | 公司规模等级。优先按公开营业额判断；若无公开营业额，再按 dealer/network 数量判断；两者都没有时留空。 | 默认分类：`1` = 年营业额低于 300 万欧元；`2` = 年营业额在 300 万欧元或以上；`3` = 营业额在 500 万欧元或以上，或者 dealer/network 在 100-500 个之间；`4` = 营业额在 1000 万欧元或以上，或者 dealer/network 超过 500 个；`5` = 营业额在 3000 万欧元或以上，或者 dealer/network 超过 1000 个。输出时该字段只写 `1` 到 `5` 的等级值，不写中文或英文说明。 |
| CoreProductOrMainBusiness | 公司主营产品、核心产品线或主营业务。 | 优先填写一个最核心主类；如有必要，也可补充其他相关主类。默认可选项：`综合泳池设备`、`热泵`、`水泵`、`盐氯机`、`太阳能产品`、`储能电池`、`变频器`、`其他`。 |
| EstablishedYear | 公司成立年份或成立日期。 | 优先填写公开可验证的成立年份，如 `1998`；如果网页给出完整日期，也可保留原文。信息不足时留空。 |
| EmployeeCount | 公司员工人数或团队规模。 | 填公开人数信息，如 `50`、`200+`、`1,000-5,000`；信息不足时留空。 |
| AnnualRevenue | 公司公开营业额、年收入或营收区间。 | 填公开营收数据或区间，如 `$10M-$50M`、`EUR 20M`；信息不足时留空。 |
| ContactPerson | 公开联系人姓名、销售联系人或负责人。 | 填公开联系人姓名；信息不足时留空。 |
| Mail | 公开邮箱、销售邮箱或联系邮箱。 | 填公开邮箱地址；信息不足时留空。 |
| Tel | 公开联系电话、公司总机或销售电话。 | 填公开电话号码；信息不足时留空。 |
| Website | 官网首页或最相关的公司页面链接。 | 填 `https://...` 链接。 |
| Address | 公司地址、办公地址、工厂地址或公开联系地址。 | 优先填写网页公开地址；保留原网页语言和原始格式；信息不足时留空。 |
| Source | 信息来源类型。用于标记这条客户线索的获取渠道。 | 当前常用值：`网页`、`展会`、`朋友介绍`、`客户介绍`；如有其他业务场景，可由用户自定义；未知时留空。 |
| FollowUpStatus | 内部销售跟进状态，由销售后续补充。 | 留空即可。 |
