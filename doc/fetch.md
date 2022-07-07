## /fetch
```text
Dummy request方法。客户端传入一张jpg/jpeg格式的图片，后段返回图片的元信息以及识别的类型，anchor坐标
```
#### 接口状态
> 开发中

#### 接口URL
> localhost:8000/dummy/fetch

#### 请求方式
> POST

#### Content-Type
> multipart/form-data

#### 请求Body参数
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
image | /Users/crinstaniev/Dev/SRS2022/sample_images/bird_sample.jpg | Text | 是 | 手机相机截取的图片，为jpg格式
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```