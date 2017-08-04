<template>
     <div class="main">
        <h1>找回密码</h1>
        <input type="text" placeholder="账号邮箱" v-model="account">
        <div class="vertificate">
            <input type="text" placeholder="验证码" v-model="vertificateCode" class="vertificate-input">
            <button @click="send-vertificate-code" class="send-vertificate-code-btn">发送验证码</button>
        </div>
        <input type="password" placeholder="密码" v-model="password">
        <input type="password" placeholder="确认密码" v-model="surePassword">
        <button @click="checkVertification" class="sure-btn">确认</button>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            account: '',
            vertificateCode: '',
            password: '',
            surePassword: '',
        }
    },
    methods: {
        sendVertificateCode() {

        },
        checkVertification() {
            // check vertification code
            if (true) {
            }
        }
    }
}
</script>

<style scoped>
.main > * {
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
    width: 250px;
}

.send-vertificate-code-btn {
    font-size: 12px;
    background-color: #a8d18d;
    width: 80px;
    height: 3em;
    border: none;
    border-radius: 10px;
    margin-right: auto;
}

.sure-btn {
    font-size: 20px;
    display: block;
    background-color: #00af50;
    color: white;
    border: none;
    border-radius: 10px;
    width: 350px;
    height: 40px;
    margin-top: 15px;
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