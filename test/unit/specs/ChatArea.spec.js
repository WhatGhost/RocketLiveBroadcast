import Vue from 'vue'
import ElInput from '../../../node_modules/element-ui/packages/input/src/input.vue'
import ChatArea from '@/components/ChatArea'

describe('ChatArea.vue', () => {
    //it('check its default data', () => {
    //    expect(ChatArea.data).to.be.a('function')
    //    const defaultData = ChatArea.data()
    //    expect(defaultData.num).to.equal(0)
    //    expect(defaultData.message).to.equal('')
    //    expect(defaultData.nickname).to.equal('')
    //    expect(defaultData.isTeacher).to.equal(false)
    //    expect(defaultData.httpServer).to.equal(null)
    //    expect(defaultData.showEmoji).to.equal(false)
    //})
    it('check its methods', () => {
        expect(ChatArea.methods).to.have.property('connectEvent')
        expect(ChatArea.methods).to.have.property('sendMessage')
    })
    it('check its import components', () => {
        expect(ChatArea.components).to.have.property('Chat')
        expect(ChatArea.components).to.have.property('ChatItem')
    })
    it('check its computed', () => {
        expect(ChatArea.computed).to.have.property('index')
    })
    //it('测试按钮点击事件', () => {
    //    let vm = new Vue(ChangePassword).$mount()
    //    vm.newpassword1='123456'
    //    vm.newpassword2='1234567'      
    //    expect(vm.changepasswdClick()).toEqual('两次密码不一致')        
    //})  
})
