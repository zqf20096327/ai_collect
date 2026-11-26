AI 低代码 零代码 工作流 组件库 快速开发
===============

[![AUR](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)]()
[![](https://img.shields.io/badge/Author-河北尚智得-orange.svg)](https://www.szdsoft.cn/about)
[![](https://img.shields.io/badge/version-2.1.0-brightgreen.svg)](https://github.com/szdsdp/z000)

## 简介

尚智得企业数字化AI平台采用 SpringCloud 微服务架构，融合低代码、零代码能力，支持可视化拖拽配置，快速搭建费控、报销、财务共享、电子档案、SRM等各类企业应用。 平台结合Spring AI框架，全域接入AI能力，覆盖 AI 数据采集、AI 智能审批、AI 数据分析，将 AI 能力融入表单、工作流、影像识别等全业务链路。 内置主数据管理、权限管理、工作流、BPM、电子影像、凭证管理、系统监控、打印模板等全套基础组件，开箱即用，自主可控，降低开发成本，缩短项目交付周期。 深度内置SAP集成能力，可完成单据穿透、单据对接、数据同步，实现与 SAP、OA 、飞书、微信、钉钉、企微等异构系统无缝打通。
## 核心亮点

- ✅ 本地私有化部署，保障企业数据安全与自主可控
- ✅ 零代码可视化设计，低代码提供 Jar 包、组件库、模板项目，开包即用
- ✅ 深度 SAP 集成：免费提供百套 SAP 集成功能
- ✅ 全场景 AI 赋能：知识问答、数据采集、智能审批、数据分析、技能调用
- ✅ 快速构建财务共享、费控、资金、售后、订货等各类企业业务应用
- ✅ 免费安装试用，免费一对一技术支持，提供完善的开发文档及示例工程

## 技术支持

使用中遇到技术问题可以提交issue 
[Issues](https://github.com/szdsdp/z000/issues)

- 官方网站：https://www.szdsoft.cn
- 平台介绍：https://www.szdsoft.cn/platform/home
- 技术文档：https://www.szdsoft.cn/platform/online-api/overview
- 数字化AI平台部署：https://www.szdsoft.cn/platform/download
- 示例模版项目源码 ：https://github.com/szdsdp/z000 (<span style="color:red">项目运行需要先部署数字化AI平台</span>)
- 纯净模版项目源码 ：https://github.com/szdsdp/z001 (<span style="color:red">项目运行需要先部署数字化AI平台</span>)
- 添加微信：
- ![](./z000-web/images/sdpQr1.png)
- 关注公众号：
- ![](./z000-web/images/sdpQr2.png)

## 在线体验

- 演示地址：[https://sdp.szdsoft.cn:81/login](https://sdp.szdsoft.cn:81/login)

- 演示用户：

  | 登录账号  | 账号名称   | 登录密码 | 角色       |
  | --------- | ---------- | -------- | ---------- |
  | TEST_ZD01 | 制单用户01 | 2025     | 管理员权限 |
  | TEST_ZD02 | 制单用户02 | 2025     | 管理员权限 |
  | TEST_SP01 | 一级审批01 | 2025     | 审批权限   |
  | TEST_SP02 | 二级审批02 | 2025     | 审批权限   |

  


## 功能预览

![image-20261110144126310](./z000-web/images/demo01.png)

![image-20261110144126310](./z000-web/images/demo02.png)

![image-20261110144126310](./z000-web/images/demo03.png)

![image-20261110144126310](./z000-web/images/demo04.png)

![image-20261110144126310](./z000-web/images/demo05.png)

![image-20261110144126310](./z000-web/images/demo06.png)

![image-20261110144126310](./z000-web/images/demo07.png)

![image-20261110144126310](./z000-web/images/demo08.png)

![image-20261110144126310](./z000-web/images/demo09.png)

![image-20261110144126310](./z000-web/images/demo10.png)

![image-20261110144126310](./z000-web/images/demo11.png)

![image-20261110144126310](./z000-web/images/demo12.png)

![image-20261110144126310](./z000-web/images/demo13.png)

![image-20261110144126310](./z000-web/images/demo14.png)

![image-20261110144126310](./z000-web/images/demo15.png)

![image-20261110144126310](./z000-web/images/demo16.png)

![image-20261110144126310](./z000-web/images/demo17.png)

![image-20261110144126310](./z000-web/images/demo18.png)

![image-20261110144126310](./z000-web/images/demo19.png)

![image-20261110144126310](./z000-web/images/demo20.png)

![image-20261110144126310](./z000-web/images/demo21.png)

![image-20261110144126310](./z000-web/images/demo22.png)

## 前置程序
### 主数据(mdm)
- 查询主数据描述(单值)getDescA

```java
/**
 * 查询主数据描述(单值)
 * 数据源：Redis缓存
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值, 如：1000
 * @param flag      返回数据格式：0-编码.描述; 1-描述;
 * @return 数据描述   示例：flag=0返回："1000.公司总部"；flag=1返回："公司总部"
 */
 public String getDescA(String baseField, String val, String flag)

// 调用示例：查询公司代码描述
String desc = clientCore.mdm.getDescA(ClientConstMdm.CORE_CMPY, "1000", "0");
```

- 查询主数据描述(两值)getDescB

```java
/**
 * 查询主数据描述(两值)
 * 数据源：Redis缓存
 * 场景：如企业会计科目主数据，同一个会计科目编码在不同的账目表中有不同的描述，此时如需查询某个科目描述就需要传入科目表+科目编码
 * @param baseField 基础字段编码，如：CORE_ACCS
 * @param val1       基础字段值1, 如：Z001
 * @param val2       基础字段值2, 如：0051410700
 * @param flag       返回数据格式：0-编码.描述; 1-描述;
 * @return 数据描述   示例：flag=0返回："0051410700.应交增值税"；flag=1返回："应交增值税"
 */
  public String getDescB(String baseField, String val1, String val2, String flag)

  // 调用示例：查询Z001账目表下的0051410700科目描述
  String desc = clientCore.mdm.getDescB(ClientConstMdm.CORE_ACCS, "Z001", "0051410700", "0");
```

- 查询主数据描述(单值,逗号分隔)getDescD

```java
/**
 * 查询主数据描述(单值,逗号分隔)
 * 数据源：Redis缓存
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值, 如：1000,2000
 * @param flag      返回数据格式：0-编码.描述; 1-描述;
 * @return 数据描述   示例：flag=0返回："1000.公司总部,2000.河北分公司"；flag=1返回："公司总部,河北分公司"
 */
  public String getDescD(String baseField, String val, String flag)

  // 调用示例：查询1000,2000两个公司的描述
  String desc = clientCore.mdm.getDescB(ClientConstMdm.CORE_CMPY, "1000,2000", "0");
```

- 校验主数据有效性(单值)checkA

```java
/**
 * 校验主数据有效性(单值)-返回校验结果
 * 数据源：数据库
 *
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值，如：1000
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 * @return 校验结果，返回对象结构如下：
 *  public class ClientResult {
 *  private String status; //状态 S-成功；E-失败
 *  private String msg;    // 描述-具体校验结果文本
 *  private String docId;  //业务单号，可自定义
 *  private List<ClientResultMsgBox> retMsgBox = new ArrayList<>(); //消息列表
 * }
 */
  public ClientResult checkA(String baseField, String val, String tips, String flag);

  // 调用示例：
  ClientResult clientResult = clientCore.mdm.checkA(ClientConstMdm.CORE_CMPY, "2100", "制单人公司", "0");
  // 返回结构
  {
    "status":"E",
    "msg":"制单人公司无效",
    "docId":"",
    "retMsgBox": []
  }
```

- 校验主数据有效性(单值)checkAE

```java
/**
 * 校验主数据有效性(单值)-直接抛出异常
 * 数据源：数据库
 *
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值，如：1000
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 */
  public void checkAE(String baseField, String val, String tips, String flag)

  // 调用示例：
  clientCore.mdm.checkAE(ClientConstMdm.CORE_CMPY, "2100", "制单人公司", "0");
```

- 校验主数据有效性(两值)checkB

```java
/**
 * 校验主数据有效性(两值)-返回校验结果
 * 数据源：数据库
 * 场景：如校验成本中心与所属公司是否匹配
 * @param baseField 基础字段编码，如：CORE_CSTC
 * @param val1       基础字段值1，如：1000
 * @param val2       基础字段值2，如：2100000101
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 * @return 校验结果，返回对象结构如下：
 *  public class ClientResult {
 *  private String status; //状态 S-成功；E-失败
 *  private String msg;    // 描述-具体校验结果文本
 *  private String docId;  //业务单号，可自定义
 *  private List<ClientResultMsgBox> retMsgBox = new ArrayList<>(); //消息列表
 * }
 */
  public ClientResult checkB(String baseField, String val1, String val2, String tips, String flag)

  // 调用示例：
  ClientResult clientResult = clientCore.mdm.checkB(ClientConstMdm.CORE_CSTC, "1000", "2100000101", "成本中心", "0");
  // 返回结构
  {
    "status":"E",
    "msg":"成本中心2100000101与公司代码1000不匹配",
    "docId":"",
    "retMsgBox": []
  }
```

- 校验主数据有效性(两值)checkBE

```java
/**
 * 校验主数据有效性(两值)-直接抛出异常
 * 数据源：数据库
 * 场景：如校验成本中心与所属公司是否匹配
 * @param baseField 基础字段编码，如：CORE_CSTC
 * @param val1       基础字段值1，如：1000
 * @param val2       基础字段值2，如：2100000101
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 */
  public void checkBE(String baseField, String val1, String val2, String tips, String flag)

  // 调用示例：
  clientCore.mdm.checkBE(ClientConstMdm.CORE_CSTC, "1000", "2100000101", "成本中心", "0");
  // 返回结构
  {
    "status":"E",
    "msg":"成本中心2100000101与公司代码1000不匹配",
    "docId":"",
    "retMsgBox": []
  }
```

- 校验主数据有效性(三值)checkC

```java
/**
 * 校验主数据有效性(三值)-返回校验结果
 * 数据源：数据库
 * 场景：如校验账户类型+用户+银行账号是否匹配
 * @param baseField 基础字段编码，如：CORE_BKAC
 * @param val1       基础字段值1，如：2
 * @param val2       基础字段值2，如：ADMIN
 * @param val3       基础字段值2，如：620123456789
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 * @return 校验结果，返回对象结构如下：
 *  public class ClientResult {
 *  private String status; //状态 S-成功；E-失败
 *  private String msg;    // 描述-具体校验结果文本
 *  private String docId;  //业务单号，可自定义
 *  private List<ClientResultMsgBox> retMsgBox = new ArrayList<>(); //消息列表
 * }
 */
 public ClientResult checkC(String baseField, String val1, String val2, String val3, String tips, String flag)

 // 调用示例：
 ClientResult clientResult = clientCore.mdm.checkC(ClientConstMdm.CORE_BKAC, "2", "ADMIN", "620123456789", "银行账号", "0");
 // 返回结构
 {
   "status":"E",
   "msg":"账户类型:2,用户:ADMIN,银行账号:620123456789不匹配",
   "docId":"",
   "retMsgBox": []
 }
```

- 校验主数据有效性(三值)checkCE

```java
/**
 * 校验主数据有效性(三值)-直接抛出异常
 * 数据源：数据库
 * 场景：如校验账户类型+用户+银行账号是否匹配
 * @param baseField 基础字段编码，如：CORE_BKAC
 * @param val1       基础字段值1，如：2
 * @param val2       基础字段值2，如：ADMIN
 * @param val3       基础字段值2，如：620123456789
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 */
 public ClientResult checkCE(String baseField, String val1, String val2, String val3, String tips, String flag)

 // 调用示例：
 ClientResult clientResult = clientCore.mdm.checkCE(ClientConstMdm.CORE_BKAC, "2", "ADMIN", "620123456789", "银行账号", "0");
```

- 校验主数据有效性(单值,逗号分隔)checkD

```java
/**
 * 校验主数据有效性(单值，逗号分隔)-返回校验结果
 * 数据源：数据库
 * 场景：如校验多个公司代码
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值，如：1000,2000
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 * @return 校验结果，返回对象结构如下：
 *  public class ClientResult {
 *  private String status; //状态 S-成功；E-失败
 *  private String msg;    // 描述-具体校验结果文本
 *  private String docId;  //业务单号，可自定义
 *  private List<ClientResultMsgBox> retMsgBox = new ArrayList<>(); //消息列表
 * }
 */
 public ClientResult checkD(String baseField, String val, String tips, String flag)

 // 调用示例：
 ClientResult clientResult = clientCore.mdm.checkD(ClientConstMdm.CORE_CMPY, "1000,2000", "公司代码", "0");
 // 返回结构
 {
   "status":"E",
   "msg":"公司代码2000无效",
   "docId":"",
   "retMsgBox": []
 }
```

- 校验主数据有效性(单值,逗号分隔)checkDE

```java
/**
 * 校验主数据有效性(单值，逗号分隔)-直接抛出异常
 * 数据源：数据库
 * 场景：如校验多个公司代码
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值，如：1000,2000
 * @param tips      消息提醒主体(选填)，如不填则默认取基础字段名称
 * @param flag      (0-必填，不允许为空；1-可选，空不检查；2-空是有效值，检查数据库)
 */
 public ClientResult checkDE(String baseField, String val, String tips, String flag)

 // 调用示例：
 ClientResult clientResult = clientCore.mdm.checkDE(ClientConstMdm.CORE_CMPY, "1000,2000", "公司代码", "0");
```

- 查询主数据对象(单值)getObjA

```java
/**
 * 查询主数据对象(单值)
 * 数据源：Redis缓存
 *
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param val       基础字段值，如：1000
 * @param <T>       返回对象类型，如：ClientObjCmpy.class
 * @return          返回指定的类型对象
 */
 public <T> T getObjA(String baseField, String val, Class<T> clazz)

 // 调用示例
 ClientObjCmpy clientObjCmpy = clientCore.mdm.getObjA(ClientConstMdm.CORE_CMPY, "1000", ClientObjCmpy.class);
```

- 查询主数据对象(两值)getObjB

```java
/**
 * 查询主数据对象(两值)
 * 数据源：Redis缓存
 *
 * @param baseField 基础字段编码，如：CORE_ACCS
 * @param val1       基础字段值，如：Z001
 * @param val2       基础字段值，如：0051410700
 * @param <T>       返回对象类型，如：ClientObjAccs.class
 * @return          返回指定的类型对象
 */
 public <T> T getObjB(String baseField, String val1, String val2, Class<T> clazz)

 // 调用示例
 ClientObjAccs clientObjAccs = clientCore.mdm.getObjB(ClientConstMdm.CORE_ACCS, "Z001", "0051410700", ClientObjAccs.class);
```

- 查询主数据清单(全部)getListA

```java
/**
 * 查询主数据清单(全部)
 * 数据源：数据库
 *
 * @param baseField 基础字段编码，如：CORE_CMPY
 * @param clazz     返回对象类型，如：ClientObjCmpy.class
 * @return          返回指定类型的对象清单
 */
 public <T> List<T> getListA(String baseField, Class<T> clazz)

 // 调用示例
 List<ClientObjCmpy> dataList = clientCore.mdm.getListA(ClientConstMdm.CORE_CMPY, ClientObjCmpy.class);
```

- 查询主数据清单(单值)getListB

```java
/**
 * 查询主数据清单(单值)
 * 数据源：数据库
 * 场景：如根据公司代码查询下挂的成本中心清单
 *
 * @param baseField 基础字段编码，如：CORE_CSTC
 * @param val       基础字段值，如：1000
 * @param clazz     返回对象类型，如：ClientObjCstc.class
 * @return          返回指定类型的对象清单
 */
 public <T> List<T> getListB(String baseField, String val, Class<T> clazz)

 // 调用示例
 List<ClientObjCstc> dataList = clientCore.mdm.getListB(ClientConstMdm.CORE_CSTC, "1000", ClientObjCstc.class);
```

- 查询主数据清单(两值)getListC

```java
/**
 * 查询主数据清单(两值)
 * 数据源：数据库
 * 场景：如根据账户类型、户主查询银行账户清单
 *
 * @param baseField 基础字段编码，如：CORE_BKAC
 * @param val1       基础字段值，如：2
 * @param val2       基础字段值，如：100000
 * @param clazz     返回对象类型，如：ClientObjBkac.class
 * @return          返回指定类型的对象清单
 */
public <T> List<T> getListC(String baseField, String val1, String val2, Class<T> clazz)

// 调用示例
List<ClientObjBkac> dataList = clientCore.mdm.getListC(ClientConstMdm.CORE_BKAC, "2", "100000", ClientObjBkac.class);
```

- 查询字典清单getListDict

```java
/**
 * 查询字典清单
 * 数据源：Redis缓存
 *
 * @param baseField 字典类型基础字段编码，如：CORE_SYS_SUCC
 * @return          返回字典对象清单
 */
  public List<ClientObjDict> getListDict(String baseField)

// 调用示例
List<ClientObjDict> dictList = clientCore.mdm.getListDict("CORE_SYS_SUCC");
```

- 查询默认业务小类getDefaultBsub

```java
/**
 * 根据路由、结构查询下面的默认小类
 * 数据源：数据库
 *
 * @param routerCode 业务路由编码，如：SEXP_COST_01A
 * @param module     路由结构编码，如：sexpCostTripHotel
 * @return          返回业务小类对象
 */
public ClientObjBsub getDefaultBsub(String routerCode, String module)

// 调用示例
ClientObjBsub bsub = clientCore.mdm.getDefaultBsub("SEXP_COST_01A", "sexpCostTripHotel");
```

- 查询控制组编码getCtrl

```java
/**
 * 根据公司代码、控制组类型查询控制组编码
 * 数据源：数据库
 *
 * @param cmpy      公司代码，如：1000
 * @param ctrlType  控制类型，如：1-差标控制组
 * @return          返回控制组编码
 */
public String getCtrl(String cmpy, String ctrlType)

// 调用示例
String ctrl = clientCore.mdm.getCtrl("1000", "1");
```

### 工具类(tool)
- 数据权限检查(checkAuth)

```java
/**
 * 根据权限对象和权限字段值 检查是否具有对应数据权限
 *
 * @param authObjCode 权限对象编码
 * @param authVal     业务数据值，多个用逗号分隔
 * 说明： 可以包含多个字段，用逗号分割，格式为：字段编码1=字段值1,字段编码2=字段值2
 * @return 检查通过返回true 否则false
 */
public boolean checkAuth(String authObjCode, String authVal)

// 调用示例
boolean checkAuth = clientCore.tool.checkAuth("CORE_AUTH001", "CORE_CMPY=2100,CORE_CSTC=2100000101");
```

- 数据修改记录保存(clogSaveA)(单对象)

```java
/**
 * 保存业务操作日志(单条记录),记录每次业务操作变化的字段值，包括新增、修改、删除
 * @param String objNo  业务ID,单据主键ID;
 * @param String tableCode 数据库表;
 * @param String operate 操作事件，如前端界面点击的按钮;
 * @param objDataNew 新值对象;
 * @param objDataOld 旧值对象;
 */
public void clogSaveA(String objNo, cString tableCode, String operate, T objDataNew, T objDataOld)

// 调用示例
clientCore.tool.clogSaveA("1809941553104424960", "sexp_cost_header", "btn_commit", headerNew, headerOld);
```

- 数据修改记录保存(clogSaveB)(对象清单)

```java
/**
 * 保存业务操作日志(多条记录),记录每次业务操作变化的字段值，包括新增、修改、删除
 * @param String objNo  业务ID,单据主键ID;
 * @param String objId  行字段键名，用于行匹配(如有多个键值，用逗号分隔),如行号：itemNo;
 * @param String tableCode 数据库表;
 * @param String operate 操作事件，如前端界面点击的按钮;
 * @param List<T> objDataNew 新值列表;
 * @param List<T> objDataOld 旧值列表;
 */
public void clogSaveB(String objNo, String objId, String tableCode, String operate, List<T> objDataNew, List<T> objDataOld)

// 调用示例
clientCore.tool.clogSaveB("1809941553104424960", "itemNo", "sexp_cost_item", "btn_save", itemListNew, itemListOld);
```

- 业务单据锁定(lockOn)

```java
/**
 * 业务加锁
 *
 * @param lockCode 锁编码 来源于业务锁主数据；如：CORE_WF-工作流锁
 * @param lockData 锁数据 JSON数组格式：如：[{"bussId":"1809941553104424960"}, {"bussId":"1810913087927226368"}]
 * @return ClientLockRet(retCode, retMsg);
 * 加锁成功：retCode=S, retMsg=""
 * 加锁失败：retCode=错误码, retMsg=具体错误信息
 */
  public ClientLockRet lockOn(String lockCode, JSONArray lockData)

  // 调用示例
  ClientLockRet clientLockRet = clientCore.tool.lockOn("CORE_WF", jsonArray);
```

- 业务单据解锁(lockOff）

```java
/**
 * 业务解锁
 *
 * @param lockCode 锁编码 来源于业务锁主数据；如：CORE_WF-工作流锁
 * @param lockData 锁数据 JSON数组格式：如：[{"bussId":"1809941553104424960"}, {"bussId":"1810913087927226368"}]
 * @return ClientLockRet(retCode, retMsg);
 * 解锁成功：retCode=S, retMsg=""
 * 解锁失败：retCode=错误码, retMsg=具体错误信息
 */
  public ClientLockRet lockOff(String lockCode, JSONArray lockData)

  // 调用示例
  ClientLockRet clientLockRet = clientCore.tool.lockOff("CORE_WF", jsonArray);
```

- 生成单据号-业务类型(getNumDocA)

```java
/**
 * 根据业务类型、子对象值生成业务单据号
 * 说明：一个完整的业务单据号组成：前缀+子对象值+日期流水。子对象作为可选值，根据实际需求确定是否需要
 * @param bstp     业务类型(必填)
 * @param subObj   子对象(选填)
 * @return ClientResult(status, msg, docId)
 * 返回说明：成功返回的单据号赋值在字段：docId；失败返回的错误码、错误信息赋值在字段：status msg
 */
  public ClientResult getNumDocA(String bstp, String subObj)

  // 调用示例
  ClientResult clientResult = clientCore.tool.getNumDocA("EXP001", "1000");

  // 返回示例
  {
      "status":"S",
      "msg":"",
      "docId":"CL2023041100001"
  }
  或
  {
      "status":"E",
      "msg":"获取单据号失败",
      "docId":""
  }
```

- 生成单据号-号码对象(getNumDocB)

```java
/**
 * 根据号码对象、子对象值生成业务单据号
 * 说明：一个完整的业务单据号组成：前缀+子对象值+日期流水。子对象作为可选值，根据实际需求确定是否需要
 * @param numObj   号码对象(必填)
 * @param subObj   子对象(选填)
 * @return ClientResult(status, msg, docId)
 * 返回说明：成功返回的单据号赋值在字段：docId；失败返回的错误码、错误信息赋值在字段：status msg
 */
 public ClientResult getNumDocB(String numObj, String subObj)

 // 调用示例
 ClientResult clientResult = clientCore.tool.getNumDocB("EXP_CL", "1000");

  // 返回结构
  {
      "status":"S",
      "msg":"",
      "docId":"CL2023041100001"
  }
  或
  {
      "status":"E",
      "msg":"获取单据号失败",
      "docId":""
  }
```
- 生成批量单据号-号码对象(getNumDocC)

```java
/**
 * 根据号码对象、子对象值批量生成业务单据号
 * 说明：一个完整的业务单据号组成：前缀+子对象值+日期流水。子对象作为可选值，根据实际需求确定是否需要
 * @param numObj   号码对象(必填)
 * @param subObj   子对象(选填)
 * @param count    生成数量
 * @return ClientResult(status, msg, docId)
 * 返回说明：成功返回的批量单据号赋值在字段：docIdList；失败返回的错误码、错误信息赋值在字段：status msg
 */
 public ClientResult getNumDocC(String numObj, String subObj, int count)

 // 调用示例
 ClientResult clientResult = clientCore.tool.getNumDocC("EXP_CL", "1000", 5);

  // 返回结构
  {
      "status":"S",
      "msg":"",
      "docIdList":["CL2023041100001", "CL2023041100002", "CL2023041100003", "CL2023041100004", "CL2023041100005"]
  }
  或
  {
      "status":"E",
      "msg":"获取单据号失败",
      "docIdList":[]
  }
```

- 生成流水号(getNumSeq)

```java
/**
 * 生成全局唯一流水号，常用作数据表的主键ID
 */
 public String getNumSeq()

 // 调用示例
 String numSeq = clientCore.tool.getNumSeq();
```

- 下载数据模板(getDownTm)

```java
/**
 * 下载Excel数据模板,通过接口从CORE平台查询文件流
 *
 * @param tmCode 模板编码
 * @return byte[] 字节流
 */
 public byte[] getDownTm(String tmCode)

 // 调用示例
 byte[] bytes = clientCore.tool.getDownTm("CORE_TM_USER");
```

- 查询全局参数(单值)(getGlobalConfigVal)

```java
/**
 * 获取全局参数-单值类型
 *
 * @param  入参格式：configType:configKey。 如：CORE_SYS_CONFIG:sys.upload.fileSize
 * @return String 返回该configKey对应的configValue
 */
 public String getGlobalConfigVal(String configType)

 // 调用示例
 String uploadFileSize = clientCore.tool.getGlobalConfigVal("CORE_SYS_CONFIG:sys.upload.fileSize");
```

- 查询全局参数(清单)(getGlobalConfigList)

```java
/**
 * 获取全局参数-清单类型
 *
 * @param configType 参数类型，如：CORE_SYS_CONFIG
 * @return List<String> 返回该configType对应的configValue字符串集合
 */
 public List<String> getGlobalConfigList(String configType)

 // 调用示例
 List<String> configList = clientCore.tool.getGlobalConfigList("CORE_SYS_CONFIG");
```

- 查询全局参数(MAP)(getGlobalConfigMap)

```java
/**
 * 获取全局参数-Map清单
 *
 * @param configType 参数类型，如：CORE_SYS_CONFIG
 * @return Map<String, String> 返回该configType对应的<configKey, configValue> Map集合
 */
 public Map<String, String> getGlobalConfigMap(String configType)

 // 调用示例
 Map<String, String> configMap = clientCore.tool.getGlobalConfigMap("CORE_SYS_CONFIG");
```

- 获取应用系统清单(getGlobalConfigSystList)

```java
/**
 * 获取应用系统-清单
 *
 * @return List<ClientObjSyst>
 * 返回结构如下：
 * [
 *  {
 *   "sysCode": "CORE",
 *   "sysName": "基础平台",
 *   "sysWebIp": "http://192.168.101.172:81",
 *   "sysWebRouter": "core",
 *   "sysJavaRouter": "/core/**,/api/**,/app/core/**",
 *   "proCode": "",
 *   "remark": "",
 *   "database": "szd-core"
 *  }
 * ]
 */
  public List<ClientObjSyst> getGlobalConfigSystList()

  // 调用示例
  List<ClientObjSyst> sysList = clientCore.tool.getGlobalConfigSystList();
```

- 外围系统接口监控报文-源报文(monLogSaveA)

```java
/**
 * 接口监控日志记录-源报文
 *
 * @param sourceHead 源标识
 * @param sourceBody 源报文
 * ClientDestination 结构如下：
 * {
 *   "destId": "SDOP",
 *   "bussTp": "FSSC001",
 *   "messId": "",
 *   "bussDoc": "BX28002410280008",
 *   "bussDocOs": "",
 *   "status": "",
 *   "messText": ""
 * }
 */
  public void monLogSaveA(ClientDestination sourceHead, String sourceBody)

  // 调用示例
  clientCore.tool.monLogSaveA(head，body);
```

- 外围系统接口监控报文-返回报文(monLogSaveB)

```java
/**
 * 接口监控日志记录-返回报文
 *
 * @param destHead 返回标识
 * @param destBody 返回报文
 * @param messId   消息ID
 * ClientDestination 结构如下：
 * {
 *   "destId": "SDOP",
 *   "bussTp": "FSSC001",
 *   "messId": "",
 *   "bussDoc": "BX28002410280008",
 *   "bussDocOs": "",
 *   "status": "",
 *   "messText": ""
 * }
 */
 public void monLogSaveB(ClientDestination destHead, String destBody, String messId)

  // 调用示例
  clientCore.tool.monLogSaveB(head，body, "1849012224743792640");
```

- 外围系统接口监控报文-更新抬头(monLogSaveC)

```java
/**
 * 接口监控日志记录-更新报文头
 *
 * @param head 系统标识
 */
 public void monLogSaveC(ClientDestination head)

 // 调用示例
 clientCore.tool.monLogSaveC(head);
```

- 消息发送-短信(sendSms)

```java
/**
 * 发送短信
 *
 * @param smsType 短信类型(A-验证码；B-待办通知；C-xx通知)
 * @param tels   接收用户，多个手机号用英文逗号分割。
 * @param msg    短信内容变量值，根据实际短信类型对应的变量，如验证码短信，只需要传入验证码值即可 map<"key1","12345">
 */
 public void sendSms(String smsType, String tels, Map<String, String> msg)

 // 调用示例
 Map<String, String> msgMap = new HashMap<String, String>();
 msgMap.put("key1", "12345");
 clientCore.tool.sendSms("A"，"18611112222,13588883333", msgMap);
```

- 消息发送-邮件(sendEmail)

```java
/**
 * 发送邮件
 * @param subject  邮件主题
 * @param toAddrs  收件人，多个地址用英文逗号分割。如：aaa@163.com,bbb@163.com
 * @param ccAddrs  抄送人，多个地址用英文逗号分割。
 * @param msg      邮件内容
 */
 public void sendEmail(String subject, String toAddrs, String ccAddrs, String msg)

  // 调用示例
  String toAddrs = "12@qq.com,34@qq.com";
  String ccAddrs = "56@qq.com,78@qq.com";
  clientCore.tool.sendEmail("提醒邮件"，toAddrs , ccAddrs , "请尽快处理您的待办事项");
```

- 消息发送-三方APP(sendMsgApp)

```java
/**
 * 发送企业微信消息
 *
 * @param toUser 收件人，多个用户用英文逗号分割。
 * @param msg    消息内容
 */
 public void sendWeixin(String toUser, String msg)

 // 调用示例
 String toUsers = "zhangsan,lisi";
 clientCore.tool.sendWeixin(toUsers, "请尽快处理您的待办事项");
```

- 查询路由权限(getAuthOper)

```java
/**
 * 根据业务路由代码查询路由权限
 *
 * @param routerCode 业务路由
 * @return ClientAuthOper, 包含操作权限、按钮权限、字段权限等
 */
 public ClientAuthOper getAuthOper(String routerCode)

 // 调用示例：
 ClientAuthOper authOper = clientCore.tool.getAuthOper("SEXP_COST_01A");
 //返回结构
{
  "struct": [
    {
      "tableType": "A",
      "tableCode": "wfBussBase",
      "cols": [
        {
          "fieldName": "实际报账金额",
          "fieldCode": "amtActual"
        },
        {
          "fieldName": "实际报账税额",
          "fieldCode": "amtActualTax"
        }
      ],
      "rowKey": "bussId",
      "tableName": "业务单据主体表"
    }
  ],
  "szdbtn": {
    "take": "3",
    "tran1": "3",
    "auto": "3",
    "print": "3",
    "rev": "3",
    "tran0": "3",
    "tran": "3"
  },
  "szddst": {},
  "szdfst": {},
  "szdopt": "U"
}
```

- 查询指定语言的翻译内容(getLangTrans)

```java
/**
 * 获取指定语言的翻译内容
 *
 * @param langSrc  源内容
 * @param langCode 语言代码
 */
 public String getLangTrans(String langSrc, String langCode)

 // 调用示例：
 String langDest = clientCore.tool.getLangTrans("你好", "en");
 // 返回:  hello
```

- 查询指定语言的消息内容(getMessage)

```java
/**
 * 获取指定语言的消息内容
 *
 * @param msgClass 消息类
 * @param msgCode  消息编号
 * @param lang     语言代码
 */
 public String getMessage(String msgClass, String msgCode, String lang)

  // 调用示例：具体参数参考：基础平台-开发管理-全局参数-消息配置
  String msg = clientCore.tool.getMessage("CORE_CLIENT"，"1", "en");
  // 返回:  Save Success
```

- 发送队列消息(sendMqMsg)

```java
/**
 * 发送队列消息-公用
 *
 * @param topic    消息主题
 * @param obj      消息体
 */
 public void sendMqMsg(String topic, Object obj)

 // 调用示例：
 MonLoginLog loginLog = new MonLoginLog();
 loginLog.setUserId("ADMIN");
 loginLog.setIpaddr("127.0.0.1");
 loginLog.setBrowser("Chrome");
 loginLog.setOs("WIN 11");
 loginLog.setMsg("登录成功");

 clientCore.tool.sendMqMsg("MQ_LOG_LOGIN"，loginLog);
```

- 发送队列消息-子主题(sendMqMsg)

```java
/**
 * 发送队列消息-公用
 *
 * @param topic    消息主题
 * @param topicSub 队列业务类型
 * @param obj      消息体
 */
 public void sendMqMsg(String topic, String topicSub, Object obj)

 // 调用示例：
 MonLoginLog loginLog = new MonLoginLog();
 loginLog.setUserId("ADMIN");
 loginLog.setIpaddr("127.0.0.1");
 loginLog.setBrowser("Chrome");
 loginLog.setOs("WIN 11");
 loginLog.setMsg("登录成功");

 clientCore.tool.sendMqMsg("MQ_LOG_LOGIN"，"A", loginLog);
```

- 消息字符串转换为message box格式(getMsgBox)

```java
/**
 * 消息字符串转换为message box格式
 *
 * @param status 状态码
 * @param msg    消息内容
 * @return List<ClientResultMsgBox>
 */
 public List<ClientResultMsgBox> getMsgBox(String status, String msg)

 // 调用示例：
 List<ClientResultMsgBox> msgBoxList = clientCore.tool.getMsgBox("E"，"检查不通过");
 // 返回结构如下
 [{
  "light": "1",
  "msgType": "",
  "retCode": "E",
  "retMsg": "检查不通过"
 }]
```

- 平台分页对象转换为SAP分页对象(getSapRangePage)

```java
/**
 * 平台分页对象转换为SAP分页对象
 * @param clientQueryPage     平台分页对象
 * @return ClientQueryPageSap SAP分页对象

 * 入参结构
 * ClientQueryPage {
 *   /** 分页 */
 *   private Integer pageNum;
 *   private Integer pageSize;
 *   /**查询条件*/
 *   private Map<String, List<ClientRangeQuery>> ranges;
 * }

 * 返回结构
 * ClientQueryPageSap {
 *   /** 分页大小 */
 *   private int pagSize;
 *   /** 查询开始页 */
 *   private int nextTag;
 *  /** 行项目 */
 *  private List<ClientRange> items;
 * }
 */
 public ClientQueryPageSap getSapRangePage(ClientQueryPage clientQueryPage)

 // 调用示例：
 ClientQueryPageSap sapQueryPage = clientCore.tool.getSapRangePage(new ClientQueryPage());
```

- 平台查询range对象转换为SAP range对象(getSapRange)

```java
/**
 * 平台查询range对象转换为SAP range对象
 * @param ranges             平台range对象
 * @return List<ClientRange> SAP range对象

 * 入参结构
 * ClientRangeQuery {
 *   private String option;
 *   private String low;
 *   private String high;
 *   private String type;
 * }

 * 返回结构
 * ClientRange {
 *   private String filename;
 *   private String sign;
 *   private String option;
 *   private String low;
 *  private String high;
 * }
 */
 public List<ClientRange> getSapRange(Map<String, List<ClientRangeQuery>> ranges)

 // 调用示例：
 Map<String, List<ClientRangeQuery>> ranges = new HashMap<>();
 List<ClientRange> retList = clientCore.tool.getSapRange(ranges);
```

### 工作流(wf)
- 检查动态流程(dyCheck)

```java
/**
 * 检查动态流程
 * @param bstp       业务类型编码
 * @param wfDyId     动态流程编号
 * @return ClientResult
 */
 public ClientResult dyCheck(String bstp, String wfDyId)

 // 调用示例
 ClientResult clientResult = clientCore.wf.dyCheck("EXP001", "0000000008");

 // 返回结构
 {
     "status":"S",
     "msg":"",
     "docId":"0000000008"
 }
 或
 {
     "status":"E",
     "msg":"动态流程不存在",
     "docId":""
 }
```

- 检查动态流程(dyCheck)

```java
/**
 * 检查动态流程-指定用户
 *
 * @param bstp   业务类型编码
 * @param userId 用户ID
 * @param wfDyId 动态流程ID
 * @return ClientResult
 */
 public ClientResult dyCheck(String bstp, String userId, String wfDyId)

 // 调用示例
 ClientResult clientResult = clientCore.wf.dyCheck("EXP001", "ADMIN", "0000000008");

 // 返回结构
  {
      "status":"S",
      "msg":"",
      "docId":"0000000008"
  }
  或
  {
      "status":"E",
      "msg":"动态流程不存在",
      "docId":""
  }
```

- 查询动态流程(dyGetObj)

```java
/**
 * 查询动态流程
 *
 * @param userId 动态流程用户
 * @param wfDyId 动态流程ID
 * @return ClientWfDyInfo 动态流程对象
 *  {
 *   "wfId": "流程ID",
 *   "userId": "流程用户",
 *   "wfDyId": "动态流程ID",
 *   "wfDyName": "动态流程名称",
 *   "active": "是否激活（0激活，1未激活）",
 *   "delFlag": "删除标记（D删除）"
 *  }
 */
  public ClientWfDyInfo dyGetObj(String wfDyId)

  // 调用示例
  ClientWfDyInfo clientWfDyInfo = clientCore.wf.dyGetObj("ADMIN", "0000000008");
```

- 查询流程操作权限(wfInit)

```java
/**
 * 查询流程操作权限
 *
 * @param bussId 业务流程ID
 * @param userId 用户ID
 * @param option 流程操作(V-查看；U-修改),先区分显示还是修改
 * @return ClientWfOper   流程操作权限
 * 结构如下：
 * String userId; 用户
 * String bussId; 业务ID
 * String bussDocId; 业务单据号
 * String bstp; 业务类型
 * String routerCode; 业务路由
 * String dyWfId; 动态流程
 * ClientWfDef wfDef; 流程缺省值(wfDyId-动态流程编号、wfDyName-动态流程名称)
 * ClientWfBtn wfBtn; 流程按钮(返回空-按钮灰色，不能点击；V-按钮能点击，不能进行附加功能操作；U-按钮能点击，附加功能可操作)
 * ClientAuthOper wfOper; 字段状态
 */
 public ClientWfOper wfInit(String bussId, String userId, String option)

 // 调用示例
 ClientWfOper clientWfOper = clientCore.wf.wfInit("1351291293123041", "ADMIN", "U");
```

- 检查流程按钮权限(wfCheckBtn)

```java
/**
 * 检查流程按钮权限与目标权限是否一致
 *
 * @param bussId  单据ID
 * @param userId  操作用户
 * @param option  目标权限(V-查看；U-编辑)
 * @param operate 流程操作事件(保存-btn_save；提交-btn_commit；审批-btn_approve；拒绝-btn_reject；
 *                撤回-btn_revoke；前加签-btn_preAddSign；后加签-btn_postAddSign；
 *                转办-btn_transfer；作废-btn_delete)
 * @return ClientResult
 */
 public ClientResult wfCheckBtn(String bussId, String userId, String option, String operate)

 // 调用示例
 ClientResult clientResult = clientCore.wf.wfCheckBtn("1351291293123041", "ADMIN", "U", "but_commit");
 // 返回结构
 {
     "status":"S",
     "msg":"检查通过",
     "docId":""
 }
 或
 {
     "status":"E",
     "msg":"无提交权限",
     "docId":""
 }
```

- 检查是否需要调用工作流(wfCheckEvt)

```java
/**
 * 检查是否需要调用工作流
 *
 * @param operate 流程操作事件(保存-btn_save；提交-btn_commit；审批-btn_approve；拒绝-btn_reject；
 *                撤回-btn_revoke；前加签-btn_preAddSign；后加签-btn_postAddSign；
 *                转办-btn_transfer；作废-btn_delete)
 */
 public boolean wfCheckEvt(String operate)

 // 调用示例
 boolean clientResult = clientCore.wf.wfCheckEvt("but_commit");
```

- 设置流程字段(wfSetField)

```java
/**
 * 设置流程字段，将界面的字段值转换到流程字段值
 * @param t 业务对象，如：差旅报账抬头CostHeader
 * @return 流程字段集合 Map<fieldCode, fieldValue>
 */
 public <T> Map<String, String> wfSetField(T t)

 // 调用示例
 CostHeader costHeader = new CostHeader();
 Map<String, String> fieldMap = clientCore.wf.wfSetField(costHeader);
```

- 调用工作流(wfCall)

```java
/**
 * 调用流程引擎处理业务
 * @param wfParam   流程参数对象
 *        wfParamEvt 操作事件、处理人、审批意见等
 *        wfParamBuss 单据ID、流程字段
   ClientWfParam 数据结构：
                /** 操作参数 */
                private ClientWfParamEvt wfParamEvt;
                /** 业务参数 */
                private ClientWfParamBuss wfParamBuss;
  ClientWfParamEvt 数据结构：
                /** 处理人 */
                private String userId;
                /** 功能按钮(提交、审批、拒绝...) */
                private String operate;
                /** 审批意见 */
                private String comments;
                /** 转办人 */
                private String tranUserId;
                /** 加签人 */
                private String addUserId;
                /** @用户 */
                private String noticeUserIds;
                /** 下一审批人 */
                private String nextUserId;
  ClientWfParamBuss 数据结构：
                /** 单据id */
                private String bussId;
                /** 流程字段 */
                private Map<String, String> wfFileds;

* @return ClientWfReturn 流程返回结果对象
  ClientWfReturn 数据结构：
                /** 单据ID */
                private String bussId;
                /** 业务单据号 */
                private String bussDocId;
                /** 返回状态码，Q-不执行工作流，直接退出；B、S-处理成功；C、E-流程错误 */
                private String retCodeF;
                /** 返回消息 */
                private String retMsg;
                /** 流程处理结果，包含：返回编码、描述、详细描述、下一节点实列 */
                private ClientWfResult wfResult;
                /** 操作参数，包含：功能按钮、审批意见、 待办id、加签人、转办人、@人 */
                private ClientWfParamEvt wfParamEvt;
                /** 业务参数，包含：单据ID 流程字段 */
                private ClientWfParamBuss wfParamBuss;
    ClientWfResult 数据结构：
                /**
                 * B000-处理成功(流程结束);B001-处理成功;B002-处理成功,驳回到发起人;B005-审批通过,请等待其他人审批;B006-处理成功(无审批流程);B007-已作废;B008-单据已删除;B009-单据已作废
                 * C001-未找到审批人；C002-存在多个审批人;C003-审批人不存在或冻结;
                 * E001-节点不存在;E002-节点配置错误;E003-流程已更新，请刷新待办;E004-待办不存在;E005-系统错误;E006-当前节点不允许加签;
                 * E007-节点已处理，不允许撤回;E008-单据已审批，不允许重复操作;E009-选择用户不存在;E010-@用户不存在;E011-任务池不支持转办业务;
                 * E012-转办用户不能设置为处理人;E013-超过允许时间，不允许撤回;E014-动态流程未配置或未激活(请提交人处理);E015-号码段未配置;E016-会签节点不允许作废
                 * E017-单据状态不支持撤回;E018-固化流程未配置(请联系技术人员);E019-固化流程未分配到公司(请联系技术人员);E020-动态流程未分配公司和绩效组(请联系技术人员)
                 * E021-业务单据不存在;E022-业务不支持批量处理;E023-业务单据已提交，不允许重复提交;E024-业务单据被锁定
                 * S000-处理成功;
                 * E101-业务单据bussId未赋值(请联系技术人员);E102-业务单据保存失败(请联系技术人员);
                 */
                private String retCode;
                /** 返回代码描述 */
                private String retCodeDesc;
                /** 返回详情描述 */
                private String retDetailDesc;
                /** 查找到的下一节点实例信息 */
                private ClientWfInst nextWfInst;
    ClientWfParamEvt 数据结构：详见本代码块11行
    ClientWfParamBuss 数据结构：详见本代码块26行

*/
public ClientWfReturn wfCall(ClientWfParam clientWfParam)

// 调用示例
ClientWfReturn clientWfReturn = clientCore.wf.wfCall(clientWfParam);
```

- 保存流程业务主体(baseSave)

```java
/**
 * 保存流程业务主体
 *
 * @param clientWfBussBase  业务主体参数
 * @return ClientWfResult   流程操作返回结果对象
 */
 public ClientWfResult baseSave(ClientWfBussBase clientWfBussBase)

 // 调用示例
 ClientWfResult clientWfResult = clientCore.wf.baseSave(wfBussBase);
```

- 查询流程业务主体(baseGetObj)

```java
/**
 * 查询业务主体
 *
 * @param bussId 业务单据ID
 * @return ClientWfBussBase 流程业务主体
 */
 public ClientWfBussBase baseGetObj(String bussId)

 // 调用示例
 ClientWfBussBase clientWfBussBase = clientCore.wf.baseGetObj("13613219284091284");
```

- 批量查询流程业务主体(baseGetObjBatch)

```java
/**
 * 查询业务主体-批量
 *
 * @param bussIds 业务单据ID集合
 * @return List<ClientWfBussBase> 业务主体集合
 */
 public List<ClientWfBussBase> baseGetObjBatch(List<String> bussIds)

 // 调用示例
 List<ClientWfBussBase> clientWfBussBaseList = clientCore.wf.baseGetObjBatch(bussIds);
```

- 查询流程实例(baseGetObjInst)

```java
/**
 * 查询流程实例
 *
 * @param bussId 业务单据ID
 * @return ClientWfBussInst 流程主体+流程示例
 */
 public ClientWfBussInst baseGetObjInst(String bussId)

 // 调用示例
 ClientWfBussInst clientWfBussInst = clientCore.wf.baseGetObjInst("13613219284091284");
```

- 查询业务主体内容(baseGetObjByBussDocId)

```java
/**
 * 查询业务主体
 *
 * @param routerCode 业务路由(选填)
 * @param bstp       业务类型(选填)
 * @param bussDocId  业务单号(必填)
 * @return ClientWfBussBase 业务主体
 */
 public ClientWfBussBase baseGetObjByBussDocId(String routerCode, String bstp, String bussDocId)

 // 调用示例
 ClientWfBussBase clientWfBussBase = clientCore.wf.baseGetObjByBussDocId("SEXP_COST_01A", "EXPA01", "CL28002504010001");
```

- 查询流程审批信息(wfApprInfo)

```java
/**
 * 查询流程审批信息
 *
 * @param bussId            业务单据ID
 * @return ClientWfApprInfo 流程审批记录
 */
 public ClientWfApprInfo wfApprInfo(String bussId)

// 调用示例
ClientWfApprInfo clientWfApprInfo = clientCore.wf.wfApprInfo("13613219284091284");
```

- 查询流程当前审批节点信息(wfApprInfoCurr)

```java
/**
 * 查询流程当前审批节点信息
 *
 * @param bussId           业务单据ID
 * @return ClientWfComment 审批信息
 */
 public ClientWfComment wfApprInfoCurr(String bussId)

// 调用示例
ClientWfComment clientWfComment = clientCore.wf.wfApprInfoCurr("13613219284091284");
```

- 保存审批信息及评审信息(wfCommentSave)

```java
/**
 * 保存审批信息及评审信息
 *
 * @param ClientApproveRet 审批信息实体
 * @return ClientWfComment 审批信息
 */
 public ClientResult wfCommentSave(ClientApproveRet clientApproveRet)

// 调用示例
ClientResult clientResult = clientCore.wf.wfCommentSave(clientApproveRet);
```

- 流程批量审批-单个审批(wfBatchApprOne)

```java
/**
 * 流程批量审批-单个审批
 *
 * @param sourceEntity      审批参数
 * @return ClientApiEntity  审批结果
 */
 public ClientApiEntity wfBatchApprOne(ClientApiEntity sourceEntity)

 // 调用示例
 ClientApiEntity clientApiEntity = clientCore.wf.wfBatchApprOne(sourceEntity);
```

- 查询用户待办清单(wfUserTodoList)

```java
/**
 * 查询用户待办清单
 *
 * @param userId    用户ID
 * @param bstpList 业务类型列表
 * @return bussIdList 单据ID列表
 */
 public List<String> wfUserTodoList(String userId, List<String> bstpList)

 // 调用示例
 List<String> bstpList = new ArrayList<String>();
 bstpList.add("EXPA01");
 bstpList.add("EXPA02");
 List<String> bussIdList = clientCore.wf.wfUserTodoList("ZHANGSAN", bstpList);
```

- 查询用户待办清单Range条件(wfUserTodoListRange)

```java
/**
 * 查询用户待办清单
 *
 * @param userId    用户ID
 * @param bstpList 业务类型列表
 * @return List<ClientRangeQuery>
 */
 public List<ClientRangeQuery> wfUserTodoListRange(String userId, List<String> bstpList)

 // 调用示例
 List<String> bstpList = new ArrayList<String>();
 bstpList.add("EXPA01");
 bstpList.add("EXPA02");
 List<ClientRangeQuery> rangeList = clientCore.wf.wfUserTodoListRange("ZHANGSAN", bstpList);
```

### 发票(inv)
- 发票验真(invCheck)

```java
/**
 * 发票验真（支持多张发票）
 *
 * @param List<ClientInvCheck> invCheckList 验真参数清单
 * @return List<ClientInvSaveRet> 验真结果
 * ClientInvCheck 结构：
 * {
 *   String invTypeCode      //发票类型
 *   String invCode          //发票代码
 *   String invNo            //发票号码
 *   String invDate          //发票日期 yyyyMMdd
 *   BigDecimal invAmtNoTax  //不含税金额
 *   BigDecimal invAmt       //价税合计金额
 *   String invCheckCode     //校验码后六位
 * }
 * ClientInvSaveRet 结构：
 * {
 *   String invCode             //发票代码
 *   String invNo               //发票号码
 *   String repeatFlag          //验重标记
 *   ClientResultMsgBox retMsg  //提示消息
 * }
 */
 public List<ClientInvSaveRet> invCheck(List<ClientInvCheck> invCheckList);

 // 调用示例
 List<ClientInvSaveRet> retList = clientCore.inv.invCheck(invCheckList);
```

- 发票保存(invSave)

```java
/**
 * 发票保存(验重、验真)
 *
 * @param List<ClientInvSave> invList 保存发票清单
 * @param List<ClientInvDel>  invDelList 解绑发票清单
 * @return List<ClientInvSaveRet> 保存结果
 *
 * ClientInvSave 结构：
 * {
 *   ClientInv header             //票面信息
 *   List<ClientInvItem> items    //发票行项目
 *   ClientInvBinding binding     //发票绑定信息
 *   Boolean itemFlag             //行项目处理标识
 *   String repeatType            //验重类型
 * }
 * ClientInvDel 结构：
 * {
 *   String bussId   //业务单据ID
 *   String invNo    //发票号码
 *   String invCode  //发票代码
 * }
 */
 public List<ClientInvSaveRet> invSave(List<ClientInvSave> invList, List<ClientInvDel> invDelList)

 // 调用示例
 List<ClientInvSaveRet> retList = clientCore.inv.invSave(invList, invDelList);
```

- 发票清单查询(getInvList)

```java
/**
 * 查询发票信息-多张
 *
 * @param List<ClientInvGetList> paramList 查询参数
 * @return List<ClientInvGetRet> 查询结果
 * ClientInvGetList 结构：
 * {
 *   String bussId          //业务单据ID(三选一必填)
 *   String eisId           //影像ID(三选一必填)
 *   String invNo           //发票号码(三选一必填)
 *   String invCode         //发票代码
 *   String invTypeCode     //票据类型
 *   String itemFlag        //查询发票行项目标识
 *   String bindingFlag     //查询发票绑定标识
 *   String fieldFlag       //查询发票字段配置标识
 * }
 * ClientInvGetRet 结构：
 * {
 *   ClientInv header                 //票面信息
 *   List<ClientInvItem> items        //发票行项目
 *   List<ClientInvBinding> bindings  //发票绑定信息
 *   List<ClientInvFieldVO> fields    //发票配置字段清单
 *   private int repeatCount          //发票绑定单据数量
 * }
 */
 public List<ClientInvGetRet> getInvList(List<ClientInvGetList> paramList)

 // 调用示例
 List<ClientInvGetRet> retList = clientCore.inv.getInvList(paramList);
```

- 查询发票信息(getInvInfo)

```java
/**
 * 查询发票信息-单张
 *
 * @param ClientInvGetList param 查询参数
 * @return ClientInvGetRet 查询结果
 * ClientInvGetList 结构：
 * {
 *   String bussId          //业务单据ID(三选一必填)
 *   String eisId           //影像ID(三选一必填)
 *   String invNo           //发票号码(三选一必填)
 *   String invCode         //发票代码
 *   String invTypeCode     //票据类型
 *   String itemFlag        //查询发票行项目标识
 *   String bindingFlag     //查询发票绑定标识
 *   String fieldFlag       //查询发票字段配置标识
 * }
 * ClientInvGetRet 结构：
 * {
 *   ClientInv header                 //票面信息
 *   List<ClientInvItem> items        //发票行项目
 *   List<ClientInvBinding> bindings  //发票绑定信息
 *   List<ClientInvFieldVO> fields    //发票配置字段清单
 *   private int repeatCount          //发票绑定单据数量
 * }
 */
 public ClientInvGetRet getInvInfo(ClientInvGetList param)

 // 调用示例
 ClientInvGetRet ret = clientCore.inv.getInvInfo(param);
```

- 发票解绑(unbinding)

```java
/**
 * 发票解绑
 * @param bussId 业务ID
 * @param delFlag 删除标记（D-逻辑删除，其他物理删除）
 */
 public void unbinding(String bussId, String delFlag)

 // 调用示例
 clientCore.inv.unbinding("1122334455", "D");
```

### 凭证(vch)
- 查询凭证模板(vchGetTm)

```java
/**
 * 查询凭证模板
 *
 * @param cmpy 公司代码
 * @param bstp 业务类型
 * @return ClientVchTemp 凭证模板
 * ClientVchTemp 结构：
 * {
 *   List<ClientVchTempItem> itemList        //凭证引擎-分录
 *   List<ClientVchTempItemField> fieldList  //凭证引擎-分录字段赋值
 * }
 */
 public ClientVchTemp vchGetTm(String cmpy, String bstp) ;

 // 调用示例
 ClientVchTemp clientVchTemp = clientCore.vch.vchGetTm("1000", "EXPA01");
```

- 生成凭证(vchGenEntry)

```java
/**
 * 生成凭证
 *
 * @param clientVchParam 参数对象(业务单据，包含业务单据头、单据行项目)
 * @return ClientVch 凭证信息
 * ClientVchParam 结构：
 * {
 *   ClientVchParamHead header          //凭证生成参数-抬头
 *   List<ClientVchParamItem> itemList  //凭证生成参数-行项目
 * }
 *
 * ClientVch 结构：
 * {
 *   ClientVchHead header          //凭证抬头
 *   List<ClientVchItem> itemList  //凭证行项目
 *   String status                 //结果状态
 *   String msg                    //状态文本
 * }
 */
 public ClientVch vchGenEntry(ClientVchParam clientVchParam)

 // 调用示例
 ClientVch clientVch = clientCore.vch.vchGenEntry(clientVchParam);
```

```java
/**
 * ClientVchHead 凭证抬头结构：
 * {
 *   String bussDocId   //业务单号
 *   String cmpy        //公司代码
 *   String vchYear     //财年
 *   String vchMonth    //期间
 *   String vchType     //凭证类型
 *   String vchDate     //凭证日期
 *   String postDate    //过账日期
 *   String postUserId  //过账人
 *   String headText    //抬头文本
 *   String headRef01   //抬头参考码1
 *   String headRef02   //抬头参考码2
 *   String curr        //币种
 *   String ifTestr     //凭证检查标识
 * }
 *
 * ClientVch 结构：
 * {
 *   Integer vchItem      //行项目号
 *   String drCr          //借贷
 *   String accs          //会计科目
 *   BigDecimal vchAmt    //凭证金额
 *   String assignNo      //分配号
 *   String summary       //项目文本
 *   String supp          //供应商
 *   String cust          //客户
 *   String sgl           //特别总账标识
 *   String busc          //业务范围
 *   String prfc          //利润中心
 *   String cstc          //成本中心
 *   String segm          //段
 *   String reas          //原因代码
 *   String transType     //事务类型
 *   String fusc          //功能范围
 *   String accType       //科目类型
 *   String orderCode     //内部订单
 *   String poDoc         //采购订单
 *   Integer poDocItem    //采购订单行项目
 *   String assetNo       //固定资产
 *   String assetNoSub    //固定资产次级编号
 *   String payTermCode   //收付条件
 *   String baseDate      //基准日期
 *   String days          //天数
 *   String taxRate       //税码
 *   String cmpyPartner   //贸易伙伴
 *   String ref01         //参考码1
 *   String ref02         //参考码2
 *   String ref03         //参考码3
 *   String material      //物料
 *   String baseQty       //基本数量
 *   String baseUnit      //基本单位
 *   String revPost       //反记账(X-反记账，其他空)
 *   String clearVchNum   //清账凭证号
 *   Integer clearVchItem //清账行项目
 *   String clearVchYear  //清账财年
 */
```

### 附件(file)
- 查询附件存储配置(getFileEds)
```java
/**
 * 查询附件类别存储配置
 *
 * @param fileCate 附件类别-根目录
 * @return ClientObjFeds 存储配置
 * ClientObjFeds 结构：
 * {
 *   String edsCode     //凭证抬头
 *   String edsName     //凭证行项目
 *   String edsType     //结果状态
 *   String edsIp       //状态文本
 *   String edsPort     //状态文本
 *   String edsUser     //状态文本
 *   String edsPwd      //状态文本
 *   String edsRoot     //状态文本
 *   BigDecimal edsSize //状态文本
 *   BigDecimal edsUsed //状态文本
 *   BigDecimal edsLimit//状态文本
 * }
 */
 public ClientObjFeds getFileEds(String fileCate)

 // 调用示例
 ClientObjFeds clientObjFeds = clientCore.file.getFileEds("IMAGE");
```

- 上传附件(uploadFile)

```java
/**
 * 上传附件
 *
 * @param fileCate 附件类别-根目录
 * @param bussPath 业务路径（根据各子应用业务自己封装，以"/"开头）
 * @param fileId   附件Id（不含扩展名）
 * @param mFile    附件
 * @return Boolean 上传结果
 */
 public Boolean uploadFile(String fileCate, String bussPath, String fileId, MultipartFile mFile)

 // 调用示例
 Boolean result = clientCore.file.uploadFile("IMAGE", "/DEV/2025/06/01/192123454599382/", "12938748734263", mFile);
```

- 下载附件-字节数组-批量(downloadFileBytesMap)

```java
/**
 * 下载附件-字节数组-批量
 *
 * @param fileCate   附件类别-根目录
 * @param remotePath 存储路径
 * @return 返回该路径下所有附件的字节数组，key为附件Id（不含拓展名）
 */
 public Map<String, byte[]> downloadFileBytesMap(String fileCate, String remotePath)

 // 调用示例
 Map<String, byte[]> resultMap = clientCore.file.downloadFileBytesMap("IMAGE", "/DEV/2025/06/01/");
```

- 下载附件-字节数组(downloadFileBytes)

```java
/**
 * 下载附件-字节数组
 *
 * @param fileCate   附件类别-根目录
 * @param remotePath 存储路径
 * @param fileId     附件Id（含拓展名）
 * @return 附件-字节数组
 */
 public byte[] downloadFileBytes(String fileCate, String remotePath, String fileId)

 // 调用示例
 byte[] result = clientCore.file.downloadFileBytes("IMAGE", "/DEV/2025/06/01/192123454599382/", "12938748734263.png");
```

- 下载附件-字节流(downloadFileStream)

```java
/**
 * 下载附件-字节流
 *
 * @param edsCode 附件存储
 * @param remotePath 存储路径
 * @param fileId   附件Id（含拓展名）
 * @return 附件-字节流
 */
 public InputStream downloadFileStream(String edsCode, String remotePath, String fileId)

 // 调用示例
 InputStream result = clientCore.file.downloadFileStream("IMAGE", "/DEV/2025/06/01/192123454599382/", "12938748734263.png");
```

- 删除附件(deleteFile)

```java
/**
 * 删除附件
 *
 * @param fileCate   附件类别-根目录
 * @param remotePath 存储路径
 * @param fileId     附件Id（含拓展名）
 * @return Boolean 删除结果
 */
 public Boolean deleteFile(String fileCate, String remotePath, String fileId)

 // 调用示例
 Boolean result = clientCore.file.deleteFile("IMAGE", "/DEV/2025/06/01/192123454599382/", "12938748734263.png");
```

- 检查附件是否存在(checkFile)

```java
/**
 * 检查附件是否存在
 *
 * @param edsCode 附件存储
 * @param remotePath 存储路径
 * @param fileId   附件Id（含拓展名）
 * @return 检查结果
 */
 public Boolean checkFile(String edsCode, String remotePath, String fileId)

 // 调用示例
 Boolean result = clientCore.file.deleteFile("IMAGE", "/DEV/2025/06/01/192123454599382/", "12938748734263.png");
```

- 移动附件(moveFile)

```java
/**
 * 移动附件
 *
 * @param fileCate    附件类别-根目录
 * @param remotePath  旧文件-存储路径
 * @param fileId      旧文件-附件Id（含拓展名）
 * @param fileCateNew 新文件-附件类别
 * @param bussPath    新文件-业务路径（根据各子应用业务自己封装，以"/"开头）
 * @param moveFlag    移动标识 move-移动 copy-复制
 * @return 删除结果
 */
 public Boolean moveFile(String fileCate, String remotePath, String fileId, String fileCateNew, String bussPath, String moveFlag)

 // 调用示例
 Boolean result = clientCore.file.moveFile("IMAGE", "/DEV/2025/06/01/192123454599382/", "12938748734263.png", "ATT", /DEV/2025/06/01/192123454599382/, "move");
```

### 应用调用(inf)
- 应用间调用原理

```java
实现源系统调用目标系统的步骤：

1）将目标系统作业程序注册到CORE作业程序配置中(配置时注意类路径和方法名必须与目标系统程序一致，否则调用失败)，用于前置根据作业程序名动态调用此作业程序的方法。

2）源系统使用clientCoreF.clientCallApi调用目标系统作业程序，此方法中head参数需指定作业程序(作业程序中已确定了目标系统)。

适用场景：应用间调用、定时任务(CORE配置定时任务)、批量审批(业务路由上配置作业程序)等。
```

- 微服务之间接口调用-记录日志(clientCallApi)

```java
/**
 * 微服务之间接口调用-记录日志
 * @param head 报文头
 * @param body 报文体
 * @return ClientApiEntity (系统标识、数据包)
 */
 public ClientApiEntity clientCallApi(ClientApiHead head, JSONObject body)

 // 调用示例
 ClientApiEntity clientApiEntity = clientCore.inf.clientCallApi(head, body);
```

- 微服务之间接口调用-不记录日志(clientCallApiN)

```java
/**
 * 微服务之间接口调用-不记录日志
 * @param head 报文头
 * @param body 报文体
 * @return ClientApiEntity (系统标识、数据包)
 */
 public ClientApiEntity clientCallApiN(ClientApiHead head, JSONObject body)

 // 调用示例
 ClientApiEntity clientApiEntity = clientCore.inf.clientCallApiN(head, body);
```

- 微服务之间接口调用-带token(clientCallApiT)

```java
/**
 * 微服务之间接口调用(先获取token再携带token调用业务接口)
 * @param head 报文头
 * @param body 报文体
 * @return ClientApiEntity (系统标识、数据包)
 */
 public ClientApiEntity clientCallApiT(ClientApiHead head, JSONObject body)

 // 调用示例
 ClientApiEntity clientApiEntity = clientCore.inf.clientCallApiT(head, body);
```

- 获取Token(clientCallToken)

```java
/**
 * 获取token
 * @param appId     应用ID
 * @param appSecret 应用密钥
 * @return token
 */
 public String clientCallToken(String appId, String appSecret)

 // 调用示例
 String token = clientCore.inf.clientCallToken("APP_SEXP", "12345");
```

- 调用SAP接口-通过平台(clientCallSap)

```java
/**
 * 通过平台统一调用SAP接口
 * @param ClientApiHead head 系统标识
 * @param JSONObject body 请求体;
 * @return ClientApiEntity
 */
 public ClientApiEntity clientCallSap(ClientApiHead head, JSONObject body)

 // 调用示例
 ClientApiEntity clientApiEntity = clientCore.inf.clientCallSap(head, body);
```

- 调用SAP接口-XML(callSapXml)

```java
/**
 * 调用SAP接口-XML
 *
 * @param ClientDestination destination 系统标识
 * @param Object params                 接口参数
 * @param Class<T> clazz                返回类型
 * @return 返回指定类类型
 */
 public <T> T callSapXml(ClientDestination destination, Object params, Class<T> clazz)

 // 调用示例
 SapApInvQueryRet sapApInvQueryRet = clientCore.inf.callSapXml(destination, params, SapApInvQueryRet.class);
```

- 调用SAP接口-JSON(callSapJson)

```java
/**
 * 调用SAP接口-JSON
 *
 * @param ClientDestination destination 系统标识
 * @param Object params                 接口参数
 * @param Class<T> clazz                返回类型
 * @return 返回指定类类型
 */
 public <T> T callSapJson(ClientDestination destination, Object params, Class<T> clazz)

 // 调用示例
 SapApInvQueryRet sapApInvQueryRet = clientCore.inf.callSapJson(destination, params, SapApInvQueryRet.class);
```

- 目标系统作业处理(目标系统作业程序)

```java
/**
 * 接口类作业程序
 */
@Service
@ClientProgApi(proCode = "SEXP_VCH_CHECK", proName = "凭证检查")
public class ProgApiVchCheck implements ClientProgApiInf {
    @Override
    public ClientApiEntity process(ClientApiEntity clientApiEntity) {
        JSONObject destBody = new JSONObject();
        ClientApiHead head = clientApiEntity.getHead();
        // 此处实现具体业务逻辑
        // ......
        return new ClientApiEntity(head, destBody);
    }
}

/**
 * 定时任务类作业程序
 */
@Service
@ClientProgJob(proCode = "SEXP_PAY_RES_QUE", proName = "付款结果查询")
public class ProgJobPayRetQuery implements ClientProgJobInf {
    @Override
    public ClientJobTaskRet process(ClientJobTaskProParam clientJobTaskProParam) {
        JSONObject destBody = new JSONObject();
        ClientApiHead head = clientApiEntity.getHead();
        // 此处实现具体业务逻辑
        // ......
        ClientJobTaskRet clientJobTaskRet = new ClientJobTaskRet();
        return clientJobTaskRet;
    }
}
```
### 电子影响(file)
- 获取 EisId (getEisId)

```java
/**
 * 获取 EisId,用于跳转影像页面
 * @param clientEisApiParam
 * @return ClientEisIdRet
 *
 * ClientEisApiParam 结构：
 * {
 *   String bussFlag     //业务标识,区分影像和附件。("img"-影像 "att"-附件)
 *   String bussId       //业务单据ID
 *   String destCode     //业务系统
 *   String infTypeCode  //接口类型
 *   String bussDocId    //业务单据号
 *   String field01      //预留字段1
 *   String field02      //预留字段2
 *   String remark       //备注
 *   String userId       //业务用户
 *   String title        //单据标题
 *   String status       //单据状态
 *   String cmpy         //公司代码
 *   String szdopt       //影像更改权限(V-查看：U-更改)
 *   String appId        //应用ID
 *   String appSecret    //应用秘钥
 * }
 *
 * ClientEisIdRet 结构：
 * {
 *   String eisId     //影像ID
 *   String szdopt    //影像更改权限(V-查看：U-更改)
 *   String retCode   //返回码
 *   String retMsg    //返回消息
 * }
 */
 public ClientEisIdRet getEisId(ClientEisApiParam clientEisApiParam)

 // 调用示例
 ClientEisIdRet ret = clientSeis.img.getEisId(clientEisApiParam);
```

- 获取 EisId -入参简化 (getEisId)

```java
/**
 * 获取 EisId（简化参数）
 * @param bussId 业务ID
 * @param destCode 外围系统
 * @param infTypeCode 接口类型
 * @return ClientEisIdRet
 */
 public ClientEisIdRet getEisId(String bussId, String destCode, String infTypeCode)

 // 调用示例
 ClientEisIdRet ret = clientSeis.img.getEisId("1351291293123041"，"SEXP"，"EXP001");
```

- 更新影像主表中的业务单据状态 (updateStatus)

```java
/**
 * 更新影像主表中的业务单据状态
 * @param bussId 业务ID
 * @param destCode 业务系统
 * @param infTypeCode 接口类型
 * @param status 单据状态(0-草稿；1-处理中；6-完成；9-作废)
 * @return 更新结果(更新成功/更新失败)
 */
  public String updateStatus(String bussId, String destCode, String infTypeCode, String status)

  // 调用示例
  String retMsg = clientSeis.img.updateStatus("1351291293123041"，"SEXP"，"EXP001", "6");
```

- 影像作废 (deleteImg)

```java
/**
 * 业务单据作废，作废影像
 * @param bussId   业务ID
 * @param destCode 业务系统
 * @param infTypeCode 接口类型
 * @param status 单据状态
 * @return 删除结果
 */
 public String deleteImg(String bussId, String destCode, String infTypeCode, String status)

 // 调用示例
 String retMsg = clientSeis.img.deleteImg("1351291293123041"，"SEXP"，"EXP001", "9");
```

- 获取影像附件 (getImgAtt)

```java
/**
 * 查询影像、附件
 * @param bussId 业务ID
 * @param flag   业务标识
 *   flag = 1 时，返回影像清单
 *   flag = 2 时，返回影像清单+文件流
 *   flag = 3 时，返回附件清单
 *   flag = 4 时，返回附件清单+文件流
 *   flag = 5 时，返回影像附件清单
 *   flag = 6 时，返回影像附件清单+文件流
 * @return List<ClientEisAttImgResult>
 *
 * ClientEisAttImgResult 结构：
 * {
 *   String eisId         //影像ID
 *   String fileId        //文件ID
 *   String fileName      //文件名称
 *   String delFlag       //删除标记
 *   String rotate        //图片旋转角度
 *   String width         //图片宽度
 *   String height        //图片高度
 *   String fileSize      //文件大小
 *   String remark        //说明
 *   String createBy      //创建人
 *   String createByName  //创建人名称
 *   String createTime    //创建时间
 *   String updateBy      //更新人
 *   String updateByName  //更新人名称
 *   String updateTime    //更新时间
 *   String ftpPath       //FTP路径
 *   String base64        //base64，文件内容
 *   String fileType      //附件类型
 * }
 */
 public List<ClientEisAttImgResult> getImgAtt(String bussId, String flag)

 // 调用示例
 List<ClientEisAttImgResult> retList = clientSeis.img.getImgAtt("1351291293123041"，"1");
```

- 根据票夹附件ID查询发票信息 (getInvListFol)

```java
/**
 * 查询票夹发票信息
 * @param ids 票夹附件ID集合
 * @return 附件基本信息+发票清单
 *
 * ClientAppFolAttachVO 结构：
 * {
 *   String attachId                    //附件编号
 *   String attachName                  //附件名称
 *   String attachPath                  //附件路径
 *   List<ClientAppFolInvVO> invList    //发票清单
 * }
 */
 public List<ClientAppFolAttachVO> getInvListFol(String ids)

 // 调用示例
 List<ClientAppFolAttachVO> retList = clientSeis.img.getInvListFol("111,222,333");
```

- 票夹报账后移动到影像 (invMoveFol)

```java
/**
 * 票夹报账，发票移动到影像
 * @param clientEisApiParam  获取eisId参数
 * @param ids  附件ID，多个用英文逗号分隔
 * @return  返回移动结果，消息盒子包含每张附件的移动结果
 */
  public List<ClientResultMsgBox> invMoveFol(ClientEisApiParam clientEisApiParam, String ids)

  // 调用示例
  List<ClientResultMsgBox> retList = clientSeis.img.invMoveFol(clientEisApiParam, "111,222,333");
```

- 单据间影像移动 (moveFile)

```java
/**
 * 单据影像附件移动，如变更单附件移动到原单
 * @param sourceBussId 源单据业务ID
 * @param targetBussId 目标单据业务ID
 */
 public void moveFile(String sourceBussId, String targetBussId)

 // 调用示例
 clientSeis.img.moveFile("1394853323908890624", "1726526867890114560");
```

## WEB组件
### 基础标签

#### Input 输入框

- 输入框（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/input-01.png)
```vue
<!-- help对象中a值'CORE_CMPY'来源于基础字段，详见[配套能力-基础字段] -->
<szd-input
  v-model="objData.val"
  showHelp
  :help="{ a: 'CORE_CMPY', b: objData, c: ['val-cmpy', 'valName-cmpyName'], j: 'valName' }" />

<szd-input-form-item
  v-model="objData.valNum"
  label="数值"
  type="number"
  numDot
  :numDec="2"
  :descSpan="10" />

<szd-input-form-item-col
  v-model="objData.val"
  label="输入框"
  showHelp
  @help="szdSh({ a: 'CORE_CMPY', b: objData, c: ['val-cmpy', 'valName-cmpyName'] })"
  :span="18"
  :descSpan="14"
  :desc="objData.valName" />

<szd-input-desc
  v-model="objData.val"
  label="输入框"
  showHelp
  :help="{ a: 'CORE_CMPY', b: objData, c: ['val-cmpy', 'valName-cmpyName'], j: 'valName' }"
  :descSpan="12"
  :desc="objData.valName" />
```

- szd-input 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String,Number |  |
| type | 是 | 类型 | String（'string' \| 'number'） | string |
| numDot | 是 | 千分位符<br>只在 type 为 'number' 的时生效 | Boolean | false |
| numDec | 是 | 小数位数<br>只在 type 为 'number' 的时生效 | Number |  |
| numMax | 是 | 最大值<br>只在 type 为 'number' 的时生效 | Number |  |
| numMin | 是 | 最小值<br>只在 type 为 'number' 的时生效 | Number |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| maxlength | 是 | 最大长度 | Number |  |
| showHelp | 是 | 显示搜索帮助 | Boolean | false |
| help | 是 | 搜索帮助<br>只在 showHelp 为 'true' 的时候生效 | Object |  |
| readonly | 是 | 仅显示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| clearable | 是 | 显示清除 | Boolean | false |
| dblclick | PC | 双击 | Boolean | false |
| clickColor | APP | 点击颜色 | Boolean | false |
| enter | 是 | 回车事件 | Boolean | false |
| align | 是 | 对齐方式 | String（'left' \| 'center' \| 'right'） | 在 type 为 'string' 的时默认左对齐<br>在 type 为 'number' 的时默认右对齐 |
| noZero | 是 | 不显示0 | Boolean | false |
| format | 是 | 格式化 | Object,String（对象：；） |  |
| required | APP | 必输 | Boolean | false |
| desc | APP | 描述 | String |  |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-input 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |
| input | 是 | 输入改变事件<br>同Element | Function |
| focus | 是 | 光标激活事件<br>同Element | Function |
| blur | 是 | 光标离开事件<br>同Element | Function |
| help | 是 | 搜索帮助事件<br>只在 showHelp 为 'true' 的时候生效<br>函数可自定义 | Function（() => void 函数可自定义也可以使用组件库方法；） |
| dblclick | PC | 双击事件<br>只在 dblclick 为 'true' 的时候生效 | Function |
| click | APP | 单击事件<br>同Varlet | Function |
| keydownEnter | 是 | 回车事件<br>同Element | Function |

- szd-input-form-item 属性（继承 szd-input 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| desc | PC | 描述 | String |  |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-input-form-item-col 属性（继承 szd-input-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

- szd-input-desc 属性（继承 szd-input 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| desc | PC | 描述 | String |  |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |

####  Input Number 数字输入框
- 数值输入框（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/inputNumber-01.png)

```vue
<szd-input-number v-model="objData.val" @change="handleChange" />

<szd-input-number-form-item v-model="objData.val" label="输入框" />

<szd-input-number-form-item-col v-model="objData.val" label="输入框" :span="12" />
```

- szd-input-number 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | Number |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| readonly | 是 | 仅显示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| max | 是 | 最大值 | Number |  |
| min | 是 | 最小值 | Number |  |
| precision | 是 | 精度 | Number |  |
| step | 是 | 步进 | Number | 1 |
| controls | PC | 控制按钮 | Boolean | true |
| required | APP | 必输 | Boolean | false |
| desc | APP | 描述 | String |  |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-input-number 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |
| focus | PC | 光标激活事件<br>同Element | Function |
| blur | PC | 光标离开事件<br>同Element | Function |

- szd-input-number-form-item 属性（继承 szd-input-number 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| desc | PC | 描述 | String |  |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-input-number-form-item-col 属性（继承 szd-input-number-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |


####  Textarea 文本域
- 文本域（PC/APP）
  ![image-20261110144126310](./z000-web/images/webapi/textArea-01.png)
```vue
<szd-textarea v-model="objData.val" @change="handleChange" />

<szd-textarea-form-item v-model="objData.val" label="文本域" />

<szd-textarea-form-item-col v-model="objData.val" label="文本域" :span="12" />
```

- szd-textarea 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| maxlength | 是 | 最大长度 | Number | 200 |
| readonly | 是 | 仅显示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| clearable | APP | 显示清除 | Boolean | false |
| rows | 是 | 显示行数 | Number | 3 |
| showWordLimit | PC | 显示字数 | Boolean | true |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-textarea 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |
| input | 是 | 输入改变事件<br>同Element | Function |
| focus | 是 | 光标激活事件<br>同Element | Function |
| blur | 是 | 光标离开事件<br>同Element | Function |
| dblclick | PC | 双击事件<br>只在 dblclick 为 'true' 的时候生效 | Function |
| click | APP | 单击事件<br>同Varlet | Function |

- szd-textarea-form-item 属性（继承 szd-textarea 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| helpTip | PC | 帮助提示 | String |  |

- szd-textarea-form-item-col 属性（继承 szd-textarea-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

####  Date 日期
- 日期（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/date-01.png)
```vue
<szd-date v-model="objData.val" @change="handleChange" />

<szd-date-form-item type="month" v-model="objData.valMonth" label="年月" />

<szd-date-form-item type="year" v-model="objData.valYear" label="年" />

<szd-date-form-item-col type="daterange" v-model="objData.valRange" label="日期范围" :span="18" />
```

- szd-date 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String,Date,Array |  |
| type | 是 | 类型 | String（PC:；） | date |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| readonly | 是 | 仅显示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| clearable | 是 | 显示清除 | Boolean | false |
| startPlaceholder | PC | 开始占位符 | String | 开始时间 |
| endPlaceholder | PC | 结束占位符 | String | 结束时间 |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-date 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |
| focus | PC | 光标激活事件<br>同Element | Function |
| blur | PC | 光标离开事件<br>同Element | Function |

- szd-date-form-item 属性（继承 szd-date 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-date-form-item-col 属性（继承 szd-date-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

#### Time 时间
- 时间（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/time-01.png)
```vue
<szd-time v-model="objData.val" @change="handleChange" />

<szd-time-form-item v-model="objData.val" label="时间" />

<szd-time-form-item-col isRange v-model="objData.valRange" label="时间范围" :span="18" />
```

- szd-time 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String,Date,Array |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| readonly | 是 | 仅显示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| clearable | 是 | 显示清除 | Boolean | false |
| startPlaceholder | PC | 开始占位符 | String | 开始时间 |
| endPlaceholder | PC | 结束占位符 | String | 结束时间 |
| required | APP | 必输 | Boolean | false |
| isRange | PC | 时间范围 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-time 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |
| focus | PC | 光标激活事件<br>同Element | Function |
| blur | PC | 光标离开事件<br>同Element | Function |

- szd-time-form-item 属性（继承 szd-time 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-time-form-item-col 属性（继承 szd-time-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

####  Select 下拉框
- 下拉框（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/select-01.png)

```vue
<!-- baseField值来源于基础字段，详见[配套能力-基础字段] -->
<szd-select
  v-model="objData.val1"
  :baseArr="[
    { svalue: 'key1', sname: '名称1' },
    { svalue: 'key2', sname: '名称2' }
  ]"
  clearable />

 <szd-select-form-item
   label="应用系统"
   v-model="objData.val2"
   baseField="CORE_SYST" />

 <szd-select-form-item-col
   label="应用系统"
   v-model="objData.val2"
   baseField="CORE_SYST"
   :span="18"
   clearable />
```

- szd-select 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String,Number,Boolean |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| baseField | 是 | 基础字段<br>baseField 和 baseArr 只能维护其中之一 | String（字段值来源于[基础字段],详见[配套能力-基础字段]） |  |
| baseArr | 是 | 范围数组<br>baseField 和 baseArr 只能维护其中之一 | Array（数据范围:；） |  |
| baseSelect | 是 | 查询条件<br>只在 baseField 有值时生效 | Array（[['字段1',值1],['字段2',值2]]） |  |
| disabled | 是 | 不可用 | Boolean | false |
| clearable | 是 | 显示清除 | Boolean | false |
| showKey | 是 | 显示Key值 | Boolean | true |
| first | 是 | 默认首个 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-select 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |

- szd-select-form-item 属性（继承 szd-select 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-select-form-item-col 属性（继承 szd-select-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |


####  Checkbox 复选框
- 复选框（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/checkbox-01.png)

```vue
<szd-checkbox v-model="objData.val" boxLabel="是否" />

<!-- baseField值来源于基础字段，详见[配套能力-基础字段] -->
<szd-checkbox
  v-model="objData.valArr1"
  :baseArr="[
    { svalue: 'key1', sname: '名称1' },
    { svalue: 'key2', sname: '名称2' }
  ]" />

 <szd-checkbox-form-item
   label="应用系统"
   v-model="objData.valArr2"
   baseField="CORE_SYST" />

 <szd-checkbox-form-item-col
   label="应用系统"
   v-model="objData.valArr3"
   baseField="CORE_SYST"
   checkboxAll="top"
   :span="18" />
```

- szd-checkbox 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | Boolean,Array |  |
| label | APP | 标签 | String |  |
| placeholder | APP | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| baseField | 是 | 基础字段<br>baseField 和 baseArr 只能维护其中之一<br>v-model 为Array时生效 | String（字段值来源于[基础字段],详见[配套能力-基础字段]） |  |
| baseArr | 是 | 范围数组<br>baseField 和 baseArr 只能维护其中之一<br>v-model 为Array时生效 | Array（数据范围:；） |  |
| direction | APP | 方向<br>v-model 为Array时生效 | String（horizontal,vertical） | horizontal |
| disabled | 是 | 不可用 | Boolean | false |
| max | 是 | 最大值<br>v-model 为Array时生效 | Number |  |
| min | 是 | 最小值<br>v-model 为Array时生效 | Number |  |
| boxLabel | 是 | 单复选框标签名称 | String |  |
| checkboxAll | 是 | 多复选框 显示全选<br>与 max 和 min不能同时使用<br>v-model 为Array时生效 | String（top 显示在上边；left 显示在左边） |  |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-checkbox 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |

- szd-checkbox-form-item 属性（继承 szd-checkbox 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-checkbox-form-item-col 属性（继承 szd-checkbox-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

####  Radio 单选
- 单选（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/radio-01.png)
```vue
<!-- baseField值来源于基础字段，详见[配套能力-基础字段] -->
<szd-radio
  v-model="objData.val1"
  :baseArr="[
    { svalue: 'key1', sname: '名称1' },
    { svalue: 'key2', sname: '名称2' }
  ]" />

 <szd-radio-form-item
   label="应用系统"
   v-model="objData.val2"
   baseField="CORE_SYST" />

 <szd-radio-form-item-col
   label="应用系统"
   v-model="objData.val2"
   baseField="CORE_SYST"
   :span="18" />
```

- szd-radio 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String,Number,Boolean |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| baseField | 是 | 基础字段<br>baseField 和 baseArr 只能维护其中之一 | String（字段值来源于[基础字段],详见[配套能力-基础字段]） |  |
| baseArr | 是 | 范围数组<br>baseField 和 baseArr 只能维护其中之一 | Array（数据范围:；） |  |
| direction | APP | 方向 | String（horizontal,vertical） | horizontal |
| disabled | 是 | 不可用 | Boolean | false |
| first | 是 | 默认首个 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-radio 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |

- szd-radio-form-item 属性（继承 szd-radio 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-radio-form-item-col 属性（继承 szd-radio-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

####  Password 密码
- 密码（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/password-01.png)

```vue
<szd-password v-model="objData.val" @change="handleChange" />

<szd-password-form-item v-model="objData.val" label="密码" />

<szd-password-form-item-col v-model="objData.val" label="密码" :span="12" />
```

- szd-password 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| maxlength | 是 | 最大长度 | Number | 200 |
| readonly | 是 | 仅显示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-password 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |
| input | 是 | 输入改变事件<br>同Element | Function |
| focus | 是 | 光标激活事件<br>同Element | Function |
| blur | 是 | 光标离开事件<br>同Element | Function |

- szd-password-form-item 属性（继承 szd-password 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| helpTip | PC | 帮助提示 | String |  |

- szd-password-form-item-col 属性（继承 szd-password-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |


#### Area 地区
- 地区（PC/APP）
  ![image-20261110144126310](./z000-web/images/webapi/area-01.png)
```vue
<szd-area v-model="objData.val" @change="handleChange" />

<szd-area-form-item v-model="objData.val" label="地区" />

<szd-area-form-item-col v-model="objData.val" label="地区" :span="12" />
```

- szd-area 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String,Number |  |
| label | APP | 标签 | String |  |
| placeholder | 是 | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| disabled | 是 | 不可用 | Boolean | false |
| clearable | 是 | 显示清除 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-area 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 更改事件<br>同Element | Function |

- szd-area-form-item 属性（继承 szd-area 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| label | PC | 标签 | String |  |
| prop | PC | model键名<br>同Element | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| descSpan | PC | 描述占位<br>0-24整数 | Number | 0 |
| helpTip | PC | 帮助提示 | String |  |

- szd-area-form-item-col 属性（继承 szd-area-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

#### Button 按钮
- 按钮（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/button-01.png)
```vue
<szd-button label="按钮" @click="handleClick" />
```

- szd-button 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| type | 是 | 按钮类型<br>同Element | String | primary |
| label | 是 | 功能名称 | String |  |
| size | APP | 大小<br>同Varlet | String |  |
| tip | PC | 提示消息 | String |  |
| text | 是 | 是否为文字按钮 | Boolean | false |
| link | 是 | 是否为链接按钮 | Boolean | false |
| disabled | 是 | 是否可用 | Boolean | false |
| notAuth | 是 | 不检查权限 | Boolean | false |
| icon | PC | 图标 | String |  |
| color | 是 | 按钮颜色 | String |  |
| hide | 是 | 是否隐藏 | Boolean | false |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-button 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| click | 是 | 点击事件<br>同Element | Function |

#### Svg 图标
- 图标（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/svg-01.png)
```vue
<szd-svg name="pc-active" clicked @click="handleClick" fixed fontSize="24" />
```

- szd-svg 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| name | 是 | svg代码 | String |  |
| fixed | 是 | 内置SVG图标 | Boolean（前端工程可以内置，也可以通过配置传输，详见[配套能力-图标管理]） | false |
| color | 是 | 颜色 | String |  |
| fontSize | 是 | 字体大小 | String |  |
| label | 是 | 标签 | String |  |
| clicked | 是 | 点击事件 | Boolean | false |

- szd-svg 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| click | 是 | 点击事件 | Function |

#### Upload 上传
- 上传（PC/APP）
![image-20261110144126310](./z000-web/images/webapi/upload-01.png)
```vue
<szd-upload-view v-model="objData.val" fileCate="DEMO_UPLOAD" acceptTxt="提示消息" :limit="3" />

<szd-upload-view-form-item
  v-model="objData.val"
  label="文本列表text"
  fileCate="DEMO_UPLOAD"
  listType="text"
  acceptTxt="提示消息-限制3个"
  :limit="3" />

<szd-upload-view-form-item
  v-model="objData.val"
  label="图片列表picture"
  fileCate="DEMO_UPLOAD"
  listType="picture"
  acceptTxt="提示消息-限制3个"
  :limit="3" />      

<szd-upload-view-form-item-col
  v-model="objData.val"
  label="图片列表picture-card"
  fileCate="DEMO_UPLOAD"
  listType="picture-card"
  acceptTxt="提示消息-限制3个"
  :limit="3"
  :span="18" />  

<szd-upload-view v-model="objData.val" label="按钮列表button" fileCate="DEMO_UPLOAD" listType="button" acceptTxt="提示消息-限制3个" :limit="3" />
```

- szd-upload-view 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | 是 | 绑定值 | String |  |
| v-model:fileCount | 是 | 文件数量 | Number |  |
| fileCate | 是 | 附件类别、附件根目录[必输]<br>在附件管理中配置 | String |  |
| filePath | 是 | 根文件后文件路径 | String |  |
| listType | 是 | 文件列表的类型 | String（'text' \| 'picture' \| 'picture-card' \| 'button'） | text |
| limit | 是 | 最大上传文件数<br>0不限制 | Number | 100 |
| fileSize | 是 | 文件大小限制<br>单位KB | Number |  |
| accept | 是 | 上传文件类型 | String |  |
| acceptTxt | 是 | 提示消息 | String |  |
| extensions | 是 | 允许的文件后缀 | Array |  |
| checkRepeat | 是 | 检查文件重复 | Boolean | true |
| download | 是 | 支持下载 | Boolean | true |
| dimension | 是 | 检查尺寸<br>[宽-最小，宽-最大，高-最小，高-最大] 数组中为数值 | Array |  |
| compress | 是 | 是否压缩图片 | Object（对象参数及默认值；） |  |
| capture | APP | 上传模式 | String（'environment' \| 'user' \| 'camera'） |  |
| cardWidth | 是 | 卡片大小-宽<br>listType=picture-card 时生效 | Number |  |
| cardHeight | 是 | 卡片大小-高<br>listType=picture-card 时生效 | Number |  |
| previewType | PC | 预览方式 | String（'A-单文件预览' \| 'B-多文件预览' \| 'C-客户化预览'） | B-多文件预览 |
| showDelete | 是 | 显示删除文件 | Boolean | false |
| bussId | 是 | 业务Id | String |  |
| bussDocId | 是 | 业务单号 | String |  |
| watermark | 是 | 水印标记 | Object（对象参数及默认值；） |  |
| disabled | 是 | 不可用 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| label | APP | 标签 | String |  |
| labelAlign | APP | 标题位置 | Object（PC端：默认left；） |  |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |

- szd-upload-view-form-item 属性（继承 szd-upload-view 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| labelAlign | PC | 标题位置 | Object（PC端：默认left；） |  |
| zip | PC | 打包下载 | Boolean | false |
| label | PC | 标签 | String |  |
| labelWidth | PC | 标签宽度<br>同Element | Number,String |  |
| required | PC | 必输 | Boolean | false |
| helpTip | PC | 帮助提示 | String |  |

- szd-upload-view-form-item-col 属性（继承 szd-upload-view-form-item 属性 和 事件）

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| span | PC | 列占位 | Number<br>0-24整数 | 12 |

- szd-upload-view 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| preview | 是 | 预览<br>previewType=C时，返回对象<br> | Function |

- szd-upload-view ref方法

| 方法名 | PC/APP | 说明 | 参数 |
| --- | --- | --- | --- |
| getFileCount | 是 | 获取文件数量-未删除ref<br>this.$ref.getFileCount() | 无 |
| getFileList | PC | 获取文件列表<br>this.$ref.getFileList() | 无 |

#### Fold 折叠
- 文件夹折叠（PC）
![image-20261110144126310](./z000-web/images/webapi/fold-01.png)
```vue
<szd-tabs-fold label="文件夹折叠">
   <div class="l-src-content">内容区域</div>
</szd-tabs-fold>
```

- szd-tabs-fold 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model:fold | PC | 折叠 | Boolean | true |
| label | PC | 标签名称 | String |  |
| border | PC | 边框 | Boolean（true 全部有线；false 打开后只有折叠框有线） | true |
| height | PC | 高度 | Number |  |

- szd-tabs-fold 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | 是 | 折叠事件 | Function |

- 上下Tabs折叠（PC）

```vue
<!-- JS变量部分 -->
SR: {
  SRH_height: 150, //抬头高度
  SRH: "Tab1",
  SRI: "Tab1"
}

<!-- VUE部分 -->
<szd-tabs-wrap :top-height="SR.SRH_height" v-model:top="SR.SRH" v-model:bottom="SR.SRI">
  <template v-slot:top>
    <el-tabs v-model="SR.SRH" type="border-card">
      <el-tab-pane name="fold">
        <template #label>
          <el-icon style="font-size: 18px; color: #1890ff">
            <FolderRemove />
          </el-icon>
        </template>
                 </el-tab-pane>
      <el-tab-pane label="信息1" name="Tab1">
        <div class="l-src-content">内容区域-信息1</div>
      </el-tab-pane>
      <el-tab-pane label="信息2" name="Tab2">
        <div class="l-src-content">内容区域-信息2</div>
      </el-tab-pane>
    </el-tabs>
             </template>
  <template v-slot:bottom>
    <el-tabs v-model="SR.SRI" type="border-card">
      <el-tab-pane name="fold">
        <template #label>
          <el-icon style="font-size: 18px; color: #1890ff">
            <FolderRemove />
          </el-icon>
        </template>
      </el-tab-pane>
      <el-tab-pane label="项目1" name="Tab1">
        <div class="l-src-content">内容区域-项目1</div>
      </el-tab-pane>
      <el-tab-pane label="项目2" name="Tab2">
        <div class="l-src-content">内容区域-项目2</div>
      </el-tab-pane>
    </el-tabs>
  </template>
</szd-tabs-wrap>
```

#### Pagination 分页
- 分页（PC/APP）
  ![image-20261110144126310](./z000-web/images/webapi/page-01.png)
```vue
<szd-pagination :total="page.total" v-model:page="page.pageNum" v-model:limit="page.pageSize" @pagination="getList" />
```

- szd-pagination 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| total | 是 | 总条数 | Number | 0 |
| v-model:page | 是 | 当前第几页 | Number | 1 |
| v-model:limit | 是 | 页大小 | Number | 20 |
| pageSizes | 是 | 页范围 | Array | PC默认[20, 50, 200, 500]<br>APP默认[20, 50, 100] |
| position | PC | 显示位置 | String（right、left） | right |
| layout | PC | 显示样式<br>同Element | String | total, sizes, prev, pager, next, jumper |
| background | PC | 显示样式<br>同Element | Boolean | true |

- szd-pagination 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| pagination | 是 | 分页事件 | Function |

#### Editor 富文本
- 富文本（PC）
  ![image-20261110144126310](./z000-web/images/webapi/editor-01.png)
```vue
<!-- 数据定义 -->
 dg: {
   uploadUrl: "#", //上传地址
   id: "id" //绑定数据的id
 }

 <!-- 标签代码 -->
 <szd-editor
   ref="szdEditor"
   :content="objData.content"
   :uploadImgUrl="dg.uploadUrl"
   :uploadAttachUrl="dg.uploadUrl"
   :params="{ id: dg.id }"
   :excludeKeys="['emotion', 'insertImage', 'insertLink', 'insertVideo', 'codeBlock', 'fmt']"
   @contentHtmlUpdate="handleContentHtmlUpdate" />

 <!-- 事件方法 -->
 handleContentHtmlUpdate(html) {
   this.objData.content = html;
 }
```

- szd-editor 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| content | PC | 文本内容 | String |  |
| hideBar | PC | 隐藏工具栏 | Boolean | false |
| placeholder | PC | 占位文本 | String | 请输入内容... |
| excludeKeys | PC | 不显示按钮/同Editor | Array |  |
| toolbarKeys | PC | 添加按钮/同Editor | Array |  |
| uploadImgUrl | PC | 上传图片到服务器地址 | String |  |
| uploadAttachUrl | PC | 上传文件到服务器地址 | String |  |
| params | PC | 上传参数 | Object |  |

- szd-editor 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| contentHtmlUpdate | PC | 更改内容触发事件 | Function |
| contentTextUpdate | PC | 更改内容触发事件 | Function |

#### Content 内容显示
- 描述显示—超宽鼠标拖动显示（PC/APP）
  ![image-20261110144126310](./z000-web/images/webapi/content-01.png)
```vue
<szd-desc :text="objData.val" />
```

- szd-desc 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| text | 是 | 内容<br>超宽鼠标滑动显示 | Number, String |  |

- 数值显示（PC/APP）

```vue
<szd-dot :text="objData.val" numDot :numDec="2" />
```

- szd-dot 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| text | 是 | 内容 | Number,String |  |
| label | APP | 标签 | String |  |
| numDec | 是 | 千分位符 | Number | false |
| numDec | 是 | 小数位数 | Number |  |
| noZero | 是 | 不显示0 | Boolean | false |
| clickColor | 是 | 高亮显示 | Boolean | false |

- 内容/代码-弹窗显示（PC）

```vue
<szd-hlt-div :code="objData.val" label="显示代码" title="代码预览" />
```

- szd-hlt-div 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| code | PC | 内容 | String |  |
| label | PC | 固定标签 | String |  |
| length | PC | 内容截取长度<br>只在 label 为空时生效 | Number |  |
| title | PC | 标题 | String | false |

- 内容/代码-直接显示（PC）

```vue
<szd-hlt :code="objData.val" />
```

- szd-hlt 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| code | PC | 内容 | String |  |
| label | PC | 固定标签 | String |  |
| length | PC | 内容截取长度<br>只在 label 为空时生效 | Number |  |
| title | PC | 标题 | String | false |

- 字段帮助提示（PC）

```vue
<szd-help-tip helpTip="ROUTER_CODE.KEY_VAL" />
```

- szd-help-tip 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| helpTip | PC | 帮助键值<br>内容维护到知识库中 | String |  |

- 文件预览-标签（PC/APP）

```vue
<!-- 标签使用 -->
<szd-file-view :src="objData.src" />

<!-- 方法调用 -->
this.szdFileView({ src: objData.src, fileName: "file.png" });
```

- szd-file-view 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| src | 是 | 地址<br>支持：图片、.docx、.xlsx、.xls、.pdf、.txt | String |  |
| fileName | 是 | 文件名 | String |  |

- 表格-列表头（PC）

```vue
<el-table-column prop="fieldId" label="字段代码" min-width="150">
  <template #header>
    <szd-table-col-header required label="字段代码" helpTip="CORE_DEV_03A.output.fieldId" />
  </template>
</el-table-column>
```

- szd-table-col-header 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| required | PC | 必输 | Boolean | false |
| label | PC | 标签 | String |  |
| helpTip | PC | 帮助提示 | String |  |
| lang | PC | 翻译 | Boolean | true |

- 交通灯（PC/APP）

```vue
<szd-light light="1" />
<szd-light light="2" />
<szd-light light="3" />
<szd-light light="0" />
```

- szd-light 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| light | 是 | 交通灯 | Number, String |  |

#### iframe 页面引用
- 页面引用（PC）
```vue
<szd-ifr
  :routerCode="objData.routerCode"
  :params="objData.params" />
```

- szd-ifr 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| routerCode | PC | 路由代码 | String |  |
| params | PC | 组件的Props参数 | Object |  |

### APP标签

#### Scan 扫码
- 扫码-输入框（APP）
  ![image-20261110144126310](./z000-web/images/webapi/appScan-01.png)
```vue
<szd-scan placeholder="扫码" v-model="test.scan" :scanCtrl="{}" clearable @change="handleChange" required />
```

- szd-scan 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | APP | 绑定值 | String |  |
| label | APP | 标签名称 | String |  |
| placeholder | APP | 占位文本 | String |  |
| hint | APP | 是否使用占位符作为提示 | Boolean | false |
| readonly | APP | 仅显示 | Boolean | false |
| disabled | APP | 不可用 | Boolean | false |
| clearable | APP | 显示清除 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| desc | APP | 描述 | String |  |
| szdfst | 是 | 字段状态 | String（1.可选  2.必输  3.仅显示、4.隐藏、5.隐藏-清空） |  |
| szdopt | 是 | 编辑状态 | String（V.仅显示） |  |
| scanCtrl | APP | 扫码参数 | Object（参数详见：szd-scan-popup 组件；） | {} |

- szd-scan 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| change | APP | 更改事件 | Function |

- 扫码-页面组件（APP）

```vue
<!-- 需要通过按钮事件调用组件 -->
<szd-scan-popup v-model:show="dg.scan.show" @scan="handleScan" />
```

- szd-scan-popup 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model:show | APP | 打开窗口 | Boolean | false |
| mode | APP | 扫码模式 | String（A.单次-自动关闭；B.连续-重复删除；C.连续-重复计数；） | A |
| formats | APP | 扫码格式<br>同vue-qrcode-reade | Array |  |
| delayTime | APP | 间隔时间-毫秒<br>在 mode 为 'B'或'C' 时生效 | Number | 100 |
| track | APP | 扫码跟踪显示框 | Boolean | false |
| constraints | APP | 扫描参数 | Object（详见官网 https://gruhn.github.io/vue-qrcode-reader/demos/Simple.html） |  |
| scanZoom | APP | 扫描图像发大缩小<br>0-终端自己控制 | Number | 100 |
| isPhoto | APP | 是否支持相册 | Boolean | true |
| isInput | APP | 是否支持录入码 | Boolean | true |
| isLight | APP | 是否支持手电筒 | Boolean | true |
| isAnimation | APP | 动画效果 | Boolean | true |

- szd-scan-popup 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| scan | 是 | 扫描结果-关闭扫描调用 | Function（返回对象；） |
| scanEvery | 是 | 扫描结果-每次扫描调用 | Function（返回序列号） |

#### Back 返回
- 顶部返回（APP）

```vue
<szd-top-back @click="handleClick" />
```

- szd-top-back 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| size | APP | 图标大小 | String,Number | 40 |

- szd-top-back 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| click | APP | 点击事件 | Function |

#### Card 卡片
- 卡片（APP）

![image-20261120-compappcard-1](./z000-web/images/webapi/appCard-01.png)

```vue
<szd-card-a v-for="row in dataList">
  <!-- 表头  -->
  <template #header>
     <szd-title-label :text="row.bussDocId" />
  </template>
  <!--  内容 -->
  <template #main>
    <span v-if="row.title" class="card-text-row">
      <div class="title">{{ $t("业务标题") }}:</div>
      <div class="content">{{ row.title }}</div>
    </span>
    <szd-card-row-span label="标签" :text="row.val" />
  </template>
  <!-- 表尾 -->
  <template #footer>
    <szd-button label="详情" type="primary" @click="handleView(row)" />
    <szd-button label="影像" type="primary" @click="handleEis(row)" />
  </template>
</szd-card-a>
```

- szd-card-a 插槽

| 插槽 | PC/APP | 说明 |
| --- | --- | --- |
| #header | 是 | 标题插槽 |
| #main | 是 | 内容插槽 |
| #footer | 是 | 表尾插槽 |

- 卡片行数据（APP）

```vue
<szd-card-a v-for="row in dataList">
  <!--  内容 -->
  <template #main>
    <szd-card-row-span label="标签1" :text="row.val" />
    <szd-card-row-span label="标签2" :text="row.val" />
  </template>
</szd-card-a>
```

- szd-card-row-span 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| text | APP | 内容 | String,Number,Boolean |  |
| label | APP | 标签 | String |  |
| align | APP | 对齐方式 | String（'left' \| 'center' \| 'right'） | right |
| numDot | APP | 千分位符 | Boolean | false |
| numDec | APP | 小数位数 | Number |  |
| clickColor | APP | 点击颜色 | Boolean | false |
| labelColor | APP | 标签颜色 | String |  |
| textColor | APP | 内容颜色 | String |  |
| labelWidth | APP | 标签宽度 | String | 28% |

- 标题显示（APP）

```vue
<szd-title-label text="标题" />
```

- szd-title-label 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| text | APP | 标题 | String |  |
| required | APP | 必输 | Boolean | false |

- 卡片行抬头（APP）

```vue
<szd-card-a v-for="row in dataList">
  <!--  卡片行：复选框、行号、删除、复制 -->
      <template #header>
        <szd-card-row-title
          v-model="row.$SZDCHECKBOX"
          :index="row.itemNo"
          checkbox
          btnCopy
          btnDelete
          @copy="handleRowCopy(row)"
          @delete="handleRowDelete(row)" />
      </template>
</szd-card-a>
```

- szd-card-row-title 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | APP | 复选框，固定字段：$SZDCHECKBOX | Boolean | false |
| text | APP | 标题内容 | String |  |
| label | APP | 标题内容（翻译） | String |  |
| index | APP | 行号 | Number，String |  |
| checkbox | APP | 启用复选框 | Boolean | false |
| required | APP | 必输 | Boolean | false |
| lighted | APP | 显示交通灯 | Boolean | false |
| light | APP | 交通灯值[1.红灯 2.黄灯 3.绿灯 其他灰灯] | Number，String | 0 |
| btnCopy | APP | 启用复制 | Boolean | false |
| btnDelete | APP | 启用删除 | Boolean | false |
| btnView | APP | 启用详情 | Boolean | false |
| disabled | APP | 不可编辑 | Boolean | false |

- szd-card-row-title 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| delete | APP | 删除行 | Function |
| copy | APP | 复制行 | Function |
| view | APP | 详情 | Function |

- 行全选（APP）

```vue
<div class="szd__popup__top" style="justify-content: space-between">
  <div>
   <!-- 全选 -->
    <szd-checkbox-all v-model:data="objData.itemList" @selection-change="handleSelRow" />
  </div>
  <div>
    <szd-button label="新增" :szdopt="SR.szdopt" @click="addRow" />
    <szd-button label="删除" :szdopt="SR.szdopt" @click="delRow" />
  </div>
</div>

// 选择行
handleSelRow(selection) {
  this.listSel = selection;
},
```

- szd-checkbox-all 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model:data | APP | 表数据，固定字段：$SZDCHECKBOX | Array |  |
| label | APP | 标签名称,false不显示 | String,Boolean | 全选 |
| disabled | APP | 不可编辑 | Boolean | false |

- szd-checkbox-all 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| selection-change | APP | 选中行 | Function |

#### List 下拉加载页
- 下拉表加载页（APP）

```vue
<szd-list :data="dataList" :total="page.total" @load="handleLoad" @refresh="handleRefresh">
  <template #default="scope">
    <szd-card-a>
      <!--  表头   -->
      <template #header>
      </template>
      <!--  内容 -->
      <template #main>
      </template>
      <!-- 表尾 -->
      <template #footer>
      </template>
    </szd-card-a>
  </template>
</szd-list>
```

- szd-list 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| pullDisabled | APP | 下拉禁用 | Boolean | false |
| loading | APP | 加载中 | Boolean | false |
| loadingText | APP | 加载描述 | String |  |
| finishedText | APP | 完成描述 | String |  |
| nothing | APP | 显示无记录 | Boolean | true |
| total | APP | 总数量 | Number | 0 |
| data | APP | 输出数据 | Array | [] |

- szd-list 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| refresh | APP | 刷新 | Function |
| load | APP | 加载新页 | Function |

#### Content 内容显示
- 文本显示（APP）

![image-20261120-compappcontentview-1](./z000-web/images/webapi/appContent-01.png)

```vue
<szd-text placeholder="文本" :text="test.text" />
```

- szd-text 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| text | APP | 内容 | Number,String |  |
| label | APP | 标签 | String |  |
| align | APP | 对齐方式 | String（'left' \| 'center' \| 'right'） | left |
| clickColor | APP | 高亮显示 | Boolean | false |

- 无文内容显示（APP）

```vue
<szd-nothing/>
```

- 弹窗标题插槽（APP）

```vue
<var-dialog v-model:show="dg.open" close-on-click-overlay @close="handleClose" :confirm-button="false" :cancel-button="false">
  <template #title>
    <szd-dialog-title title="消息提示" v-model="dg.open" @close="handleCloseForm" />
  </template>
</var-dialog>
```

- szd-dialog-title 属性

| 属性名 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- |
| v-model | APP | 绑定值-打开关闭 | Boolean |  |
| title | APP | 标题 | String | 提示 |
| close | APP | 关闭按钮 | Boolean | true |

- szd-dialog-title 事件

| 事件名 | PC/APP | 说明 | 类型 |
| --- | --- | --- | --- |
| close | APP | 关闭事件 | Function |

### 组件方法

#### Search Help 搜索帮助
- 搜索帮助原理（PC/APP）

![image-20261120-compsearchhelp-1](./z000-web/images/webapi/funcSH-01.png)

- 标签应用（PC/APP）

- szdSh方法（PC/APP）

```java
/**
 * 搜索帮助弹出框
 *
 * @param {Object} shPar 以下是对象说明
 * a:baseField[基础字段] 必填
 * b:dataObj[更改的数据(对象或数组)] :help="{}" 可选 @help="szdSh({})" 必填
 * c:baseMapping[映射关系] 如：['字段(目标)-字段(源)','字段(目标和源相同)','字段(目标)-*（*代表默认字段或第一字段）'] :help="{}" 可选 @help="szdSh({})" 必填
 * d:baseSelect[查询条件] 如：[['字段',值],['字段',值]] 可选
 * e:disabled[不能赋值] true 不可以赋值
 * f:moveType[类型]  可选 默认单选 [1单选 2多选 5多选用逗号分隔赋值-附加 6多选用逗号分隔赋值-替换]
 * g:rowIndex [多行赋值时的行号]（行赋值必传）如：scope.$index 可选
 * h:chgFields[触发change的字段] 可选 如：['字段(目标)','字段(目标)'] 可选
 * i:selectField[类型] 选中字段 可选(仅多选支持) 如：'字段(目标)-字段(源)' 或 '字段(目标和源相同)'
 * j:autoCompleteDescField[自动补全描述字段]
 *
 * @returns {Promise<res>} 返回参数说明
 * 返回对象 {data:[选中的行数据],param:{参数如默认字段},chgValue 选择的值,chgFlag:bool值 true更改 false未更改,chgField:{更改字段:{新值,旧值}}};
 * 返回boolean 直接关闭窗口返回false
 *
 * 使用说明
 * <szd-input show-help :help="{}">
 * <szd-input show-help @help="szdSh({})">
 */
 function szdSh(shPar)

 // 调用示例
 let _objData = { cmpy: "", cmpyName: "" };
 this.szdSh({ a: "CORE_CMPY", b: _objData, c: ["cmpy", "cmpyName"] }).then(res => {
 if (res && res.data && res.data.length > 0) {
    this.$mS("选中值：" + _objData.cmpy);
 } else {
    this.$mW("未选择值");
 }
 });
```

- szdSh 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | shPar | 是 | 参数 | Object（示例:{；） |  |
| - | a | 是 | 基础字段[必填] | String |  |
| - | b | 是 | 更改的数据[必填]<br>只在 f 为 '2' 的时为数组，其它为对象 | Object,Array |  |
| - | c | 是 | 映射关系[必填]<br>['字段(目标)-字段(源)','字段(目标和源相同)'] | Array |  |
| - | d | 是 | 查询条件[可选]<br>[['字段',值],['字段',值]] | Array |  |
| - | e | 是 | 不能赋值[可选] | Boolean | false |
| - | f | 是 | 类型[可选]<br>[1单选 2多选 5多选用逗号分隔赋值-附加 6多选用逗号分隔赋值-替换] | Number | 1 |
| - | g | 是 | 多行赋值时的行号<br>只在 f 为 2 的时必填 | Number |  |
| - | h | 是 | 触发change的字段[可选] | Array |  |
| - | i | 是 | 多选时已选的数据选中行[可选]<br>只在 多选时 生效 <br>'字段(目标)-字段(源)' 或 '字段(目标和源相同)' | String |  |
| - | j | 是 | 自动补全描述字段[可选]<br>只在 :help中b有值时 生效 | String |  |
| 返回 | then() | 是 | 返回 | Object,Boolean（选中数据返回 ；） |  |
| - | data | 是 | 选中的行数据 | Array |  |
| - | chgValue | 是 | 默认选择的值 | String |  |
| - | chgFlag | 是 | 值是否发生更改<br>true更改;false未更改 | Boolean |  |
| - | chaField | 是 | 更改字段 {字段:{nVal:新值,oVal:旧值} | Object |  |

- szdShow方法（PC/APP）

```java
/**
 * 调用搜索帮助窗口
 *
 * @param {Object} shPar 以下是对象说明
 * a:baseField[基础字段] 必填
 * b:dataObj[更改的数据(对象或数组)] 可选
 * d:baseSelect[查询条件] 如：[['字段',值],['字段',值]] 可选
 * f:moveType[类型]  可选 默认单选 [1单选 2多选 5多选用逗号分隔赋值-附加 6多选用逗号分隔赋值-替换]
 * i:selectField[类型] 选中字段 可选(仅多选支持) 如：'字段(目标)-字段(源)' 或 '字段(目标和源相同)'
 *
 * @returns {Promise<res>} 返回参数说明
 * 返回对象 {data:[选中的行数据],param:{参数如默认字段}}
 * 返回boolean 直接关闭窗口返回false
 */
 function szdShShow(shPar)

 // 调用示例
 this.szdShShow({ a: "CORE_CMPY" }).then(res => {
    if (res && res.data && res.data.length > 0) {
      this.$mS("选中值：" + res.data[0].cmpy);
    } else {
      this.$mW("未选择值");
    }
 });
```

- szdShow 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | shPar | 是 | 参数 | Object（示例:{；） |  |
| - | a | 是 | 基础字段[必填] | String |  |
| - | b | 是 | 更改的数据[可选]<br>只在 f 为 '2' 的时为数组，其它为对象 | Object,Array |  |
| - | d | 是 | 查询条件[可选]<br>[['字段',值],['字段',值]] | Array |  |
| - | f | 是 | 类型[可选]<br>[1单选 2多选 5多选用逗号分隔赋值-附加 6多选用逗号分隔赋值-替换] | Number | 1 |
| - | i | 是 | 多选时已选的数据选中行[可选]<br>只在 多选时 生效 <br>'字段(目标)-字段(源)' 或 '字段(目标和源相同)' | String |  |
| 返回 | then() | 是 | 返回 | Object,Boolean（选中数据返回 ；） |  |
| - | data | 是 | 选中的行数据 | Array |  |

#### Msg 消息
- 消息列表（PC/APP）
  ![image-20261120-compsearchhelp-1](./z000-web/images/webapi/funcMsg-01.png)
```java
/**
 * 消息弹窗
 *
 * @param {Array} msg 以下是对象说明 [{light:指示灯,retCode:消息码,retMsg:消息内容}]
 * light:指示灯 枚举：1.红灯 2.黄灯 3.绿灯 其它灰灯
 * retCode:消息码
 * retMsg:消息内容
 * @param {Boolean} okayFlag 显示确认按钮
 */
function szdMsgBox(msgList, okayFlag = false)

// 调用示例
this.szdMsgBox(msgList, okayFlag).then(res => {
   this.$mS("点击结果为" + res);
});
```

- szdMsgBox 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | msg | 是 | 消息内容 | Array（示例:[；） |  |
| - | light | 是 | 指示灯 | Number,String（枚举：1.红灯 2.黄灯 3.绿灯 其它灰灯） | 灰灯 |
| - | retCode | 是 | 错误代码 | String |  |
| - | retMsg | 是 | 错误消息 | String |  |
| 参数2 | okayFlag | 是 | 显示确认按钮 | Boolean | false |
| 返回 | then() | 是 | 返回 | Boolean |  |

- 确认提示（PC/APP）

```java
/**
* 确认提示
* @param {String|Array} msgText 消息
* @param {Boolean} catchFlag 关闭触发catch
*/
function szdPop(msgText = "", catchFlag = false)

// 调用示例
this.szdPop("消息内容，请确认").then(() => {
this.$mS("点击结果为then");
});

或

this.szdPop("消息内容，请确认", catchFlag)
.then(() => {
this.$mS("点击结果为then");
})
.catch(() => {
this.$mW("点击结果为catch");
});
```

- szdPop 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | msgText | 是 | 消息 | String,Array | 请确认? |
| 参数2 | catchFlag | 是 | 关闭触发catch | Boolean | false |
| 返回 | then() | 是 | 返回 | Boolean |  |
| 异常 | catch() | 是 | 返回 | Boolean |  |

- 保存提示（PC/APP）

```java
/**
 * 保存确认提示
 * @param {String|Array} msgText 消息
 * @param {Boolean} catchFlag 关闭触发catch
 */
function szdPopSave(msgText = "", catchFlag = false)

// 调用示例
this.szdPopSave().then(() => {
  this.$mS("点击结果为then");
});
```

- szdPopSave 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | msgText | 是 | 消息 | String,Array | 数据保存，请确认? |
| 参数2 | catchFlag | 是 | 关闭触发catch | Boolean | false |
| 返回 | then() | 是 | 返回 | Boolean |  |
| 异常 | catch() | 是 | 返回 | Boolean |  |

- 删除提示（PC/APP）

```java
/**
 * 删除确认提示
 * @param {String|Array} msgText 消息
 * @param {Boolean} catchFlag 关闭触发catch
 */
function szdPopDel(msgText = "", catchFlag = false)

// 调用示例
this.szdPopDel().then(() => {
this.$mS("点击结果为then");
});
```

- szdPopDel 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | msgText | 是 | 消息 | String,Array | 数据将被删除，请确认? |
| 参数2 | catchFlag | 是 | 关闭触发catch | Boolean | false |
| 返回 | then() | 是 | 返回 | Boolean |  |
| 异常 | catch() | 是 | 返回 | Boolean |  |

#### Upload 上传
- 文件上传（PC/APP）
  ![image-20261120-compsearchhelp-1](./z000-web/images/webapi/funcUpload-01.png)
```java
/**
 * 上传组件
 *  @param {Object}  updParams:{
 *    limit: 1, //最大上传文件数
 *    fileSize: undefined, //文件大小-KB
 *    dimension: [],  //尺寸[宽-最小，宽-最大，高-最小，高-最大]
 *    accept: "", //上传文件类型 如: ".xls,.xlsx"
 *    acceptTxt: "", //提示信息
 *    extensions: [], //文件后缀
 *    uploadUrl: "", //上传地址
 *    fileCate: "", //附件类别-根目录
 *    filePath: "", //文件路径
 *    bussId: "", //业务id
 *    custParam: {}, //自定义参数
 *    showMsgBox: true, //显示消息
 *    listType: "text", //文件列表的类型
 *    TMCode: "", //下载模版
 *    title:"",//窗口名称
 *    dialogWidth: 400, //窗口宽度
 *    dialogHeight: 450, //窗口高度
 *    //压缩图片
 *    compress: {
 *      compress: false, //是否压缩
 *      fileSize: 1024,  //超过多大进行压缩KB
 *      quality: 0.8, //压缩质量
 *      widthMax: 1600, //压缩最大宽度
 *      widthMin: 100   //压缩最小宽度
 *    }
 * }
 * @return {Promise} 返回参数说明
 * [{
 *    light 指示灯\tNumber、String\t枚举：1.红灯 2.黄灯 3.绿灯 其它灰灯
 *    retCode 错误代码\tstring
 *    retMsg 错误消息\tstring
 *    bussId 业务id\tString
 *    fileName 文件名\tString
 *    filePath 文件路径\tString
 * }]
 */
function szdUpload(updParams)    

// 调用示例
this.szdUpload(updParams).then(res => {
   console.log(res);
});
```

- szdUpload 参数

| 参数 | 字段 | PC/APP | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- | --- | --- |
| 参数1 | updParams | 是 | 上传参数 | Object（示例: {；） |  |
| - | limit | 是 | 最大上传文件数 | Number | 1 |
| - | fileSize | 是 | 文件大小-KB | Number |  |
| - | dimension | 是 | 尺寸 | Array（[],不控制;[宽-最小，宽-最大，高-最小，高-最大]） | [] |
| - | accept | 是 | 上传文件类型 | String |  |
| - | acceptTxt | 是 | 提示信息 | String |  |
| - | extensions | 是 | 支持文件后缀 | String（示例:xls,xlsx） |  |
| - | uploadUrl | 是 | 上传地址<br>为空时 fileCate 必须维护 | String |  |
| - | fileCate | 是 | 附件类别-根目录 | String |  |
| - | filePath | 是 | 文件路径 | String |  |
| - | bussId | 是 | 业务id | String |  |
| - | custParam | 是 | 自定义参数（提交后端参数） | Object | {} |
| - | showMsgBox | 是 | 显示消息 | Boolean | true |
| - | listType | PC | 文件列表的类型<br>同Element | String | true |
| - | TMCode | PC | 下载模板代码 | String |  |
| - | title | PC | 窗口名称 | String |  |
| - | dialogWidth | PC | 窗口宽度 | Number | 400 |
| - | dialogHeight | PC | 窗口高度 | Number | 450 |
| - | compress | 是 | 压缩图片 | Object（示例: {；） |  |
| -- | compress | 是 | 是否压缩 | Boolean | false |
| -- | fileSize | 是 | 超过多大进行压缩KB | Number | 1024 |
| -- | quality | 是 | 压缩质量 | Number | 0.8 |
| -- | widthMax | 是 | 压缩最大宽度 | Number | 1600 |
| -- | widthMin | 是 | 压缩最小宽度 | Number | 100 |
| 返回 | then() | 是 | 返回 | Array,Boolean,Object（标准接口返回（uploadUrl 为空 fileCate 有值时）；） |  |
| - | light | 是 | 指示灯 | Number,String（枚举：1.红灯 2.黄灯 3.绿灯 其它灰灯） |  |
| - | retCode | 是 | 错误代码 | String |  |
| - | retMsg | 是 | 错误消息 | String |  |
| - | bussId | 是 | 业务id | String |  |
| - | fileName | 是 | 文件名 | String |  |
| - | filePath | 是 | 文件路径 | String |  |

- EXCEL上传（PC）

```java
/**
 * 上传Excel组件-可选
 *  @param {Object}  updParams:{
 *     acceptTxt: "", //提示信息-可选
 *     TMCode: "", //下载模板-可选
 *     fileName: "", //下载文件名-可选
 *     title: "", //标题-可选
 *     dialogWidth: 300, //窗口宽度-可选
 *     dialogHeight: 300, //窗口高度-可选
 *     showData: false, //显示数据
 *     showIndex: false //显示数据时显示行号
 * }
 *
 * @param {Array} fCats 表头参数
 * [{
 *  field:列字段,
 *  label:列名称,
 *  type:数据类型-可选["string", "number", "boolean", "date", "datetime", "time", "year", "month"],
 *