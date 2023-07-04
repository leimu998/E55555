//发布留言
			Release() {
				this.token = uni.getStorageSync('token')
				uni.request({
					url: ' http://172.16.222.16:90/api/comment/add',
					method: 'POST',
					header: {
						Authorization: this.token
					},
					data: this.formMsg,
					success: (res) => {
						console.log(res);
					}
				})
			},
