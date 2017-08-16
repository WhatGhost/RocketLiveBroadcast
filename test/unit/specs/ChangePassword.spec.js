import Vue from 'vue'
import ElInput from '../../../node_modules/element-ui/packages/input/src/input.vue'
import ChangePassword from '@/components/ChangePassword'

describe('ChangePassword.vue', () => {
    it('check its default data', () => {
        expect(ChangePassword.data).to.be.a('function')
        const defaultData = ChangePassword.data()
        expect(defaultData.useraccount).to.equal('')
        expect(defaultData.oldpassword).to.equal('')
        expect(defaultData.newpassword1).to.equal('')
        expect(defaultData.newpassword2).to.equal('')
    })
    it('check its methods', () => {
        expect(ChangePassword.methods).to.have.property('changepasswdClick')
    })
    //it('测试按钮点击事件', () => {
    //    let vm = new Vue(ChangePassword).$mount()
    //    vm.newpassword1='123456'
    //    vm.newpassword2='1234567'      
    //    expect(vm.changepasswdClick()).toEqual('两次密码不一致')        
    //}) 
})
