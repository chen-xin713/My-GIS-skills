#### Vue3中使用`Composition API`（组合`API`）让相关功能的代码更加有序的组织在一起。
	Q:setup和data、methods可不可以一起写？data、methods能够获取setup中的数据吗？setup能够获取data、methods中的东西吗？
	A1:可以一起写，因为Vue3中是支持Vue2中的语法进行编写的。
	A2：能，因为setup函数会在beforeCreate之前调用，它是“领先”所有钩子执行的。
	A3：不能，同上。
