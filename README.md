# 空气质量监测

自动获取目标地的空气质量指数，如果超过150为中度污染，触发短信提醒

## 使用说明

通过[mob.com](http://api.mob.com/#/apiwiki/environment)获取实时的空气质量指数，判断后使用[阿里大于](https://www.alidayu.com/?spm=0.0.1.d10001.IQfB88)进行短信发送。

其中阿里大于使用@0x5010修改后的[短信接口](https://github.com/0x5010/alidayu)。

可直接用pip安装。

```shell
sudo pip install six
pip install alidayu
```

## 编写细节

* 用两个小时，从python零基础现学的，肯定有不少naive或者dirty的用法，还请指正。
* 代码未做多少封装，只是一个参考交流的目的。
* 以后一定会继续扩展功能，比如快递查询 天气预报等等。

## 运行效果

![Demo](http://oklhb00qa.bkt.clouddn.com/air.jpg)