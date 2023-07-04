Validate() {
				//验证账号
				if (this.formData.account.length < 6 || this.formData.account.length > 20) {
					this.errorAccount = '账号长度必须在6~20位长度'
					this.flagAccount = false
					return
				}
				this.errorAccount = '账号验证通过'
				this.flagAccount = true
				//验证密码
				if (!this.passwordRegex.test(this.formData.password)) {
					this.errorPassword = '密码必须由大写字母、小写字母和数字构成（至少包含两种），长度在6~20位长度'
					this.flagPassword = false
					return
				}
				this.errorPassword = '密码验证通过'
				this.flagPassword = true
				//验证密码重复
				if(!this.formData.password === this.formData.password2){
					this.errorPassword2 = '重复密码错误'
					this.flagPassword2 = false
					return
				}
				this.errorPassword2 = '重复密码通过'
				this.flagPassword2 = true
			}
