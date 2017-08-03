<<template>
    <div class="main">
        <h1>注册</h1>
        <input type="text" placeholder="邮箱" class="email" v-model="email"></input>
        <input type="text" placeholder="昵称" class="name" v-model="nickname"></input>
        <input type="text" placeholder="密码" class="password" v-model="password"></input>
        <input type="text" placeholder="确认密码" class="sure-password" v-model="confirmPassword"></input>
        <div class="vertificate">
            <input type="text" placeholder="验证码" class="vertificate-input" v-model="vertificateCode"></input>
            <a class="send-email-btn" href="http://www.baidu.com">发送邮件，获取验证码</a>
        </div>
        <button type="button" class="sure-btn" @click="registerBtnClick">确认</button>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            email: '',
            nickname: '',
            password: '',
            confirmPassword: '',
            vertificateCode: ''
        }
    },
    computed: {

    },
    methods: {
        isRightEmail() {
            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return re.test(this.email)
        },
        registerBtnClick() {
            if (this.email === '') {
                window.alert('请填写邮箱')
                return
            }
            if (!this.isRightEmail()) {
                window.alert('邮箱格式不正确！')
                return
            }
            if (this.nickname === '') {
                window.alert('未填写昵称')
            }
            // todo: make sure password's format
            if (this.password !== this.confirmPassword) {
                window.alert('两次密码不一致')
                return
            }
            if (this.vertificateCode === '') {
                window.alert('请填写验证码')
                return
            }
            window.alert(this.email + '\n' + this.password + '\n' + this.vertificateCode)
        },
        sendVertificateCode() {
            // not sure how we'll do this
            // maybe use method in store.js?
        }
    }
}
</script>


<style>
.main {
    margin-left: auto;
    margin-right: auto;
}

h1 {
    font-size: 24px;
    font-weight: normal;
}

input {
    display: block;
    font-size: 16px;
    border: 1px solid #e8e8e8;
    padding-left: 10px;
    width: 350px;
    height: 26px;
    margin: 5px;
    border-radius: 2px;
}

.vertificate {
    margin-left: auto;
    margin-right: auto;
}

.vertificate-input {
    display: inline-block;
    width: 150px;
}

.send-email-btn {
    font-size: 16px;
    color: #007acc;
    margin-right: auto;
}

.sure-btn {
    font-size: 20px;
    display: block;
    border: none;
    background-color: #00af50;
    color: white;
    border-radius: 10px;
    width: 350px;
    height: 40px;
    margin: 15px;
}

input::-webkit-input-placeholder {
    /* WebKit browsers */
    color: #e8e8e8;
}

input:-moz-placeholder {
    /* Mozilla Firefox 4 to 18 */
    color: #e8e8e8;
}

input::-moz-placeholder {
    /* Mozilla Firefox 19+ */
    color: #e8e8e8;
}

input:-ms-input-placeholder {
    /* Internet Explorer 10+ */
    color: #e8e8e8;
}
</style>
