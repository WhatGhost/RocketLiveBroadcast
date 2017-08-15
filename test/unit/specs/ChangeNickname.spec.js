import Vue from 'vue'
import ElInput from '../../../node_modules/element-ui/packages/input/src/input.vue'
import ChangeNickname from '@/components/ChangeNickname'
import store from '../../../src/store/store.js'

describe('ChangeNickname.vue', () => {
    it('check its default data', () => {
        expect(ChangeNickname.data).to.be.a('function')
        const defaultData = ChangeNickname.data()
        expect(defaultData.account).to.equal('')
        expect(defaultData.newnickname).to.equal('')
    })
    it('check its methods', () => {
        expect(ChangeNickname.methods).to.have.property('changeNickname')
    })
    it('测试按钮点击事件', () => {
        let vm = new Vue(ChangeNickname).$mount()
        vm.newnickname='你好世界'
        vm.changeNickname()
        // 断言组件的message是否变为了'你好世界'
        expect(vm.nickname).toEqual('你好世界')
        //vm = createTest(ChangeNickname)
        //let buttonElm = vm.$el.querySelector('el-button')
        //buttonElm.click()
        // setTimeout 的原因
        // 在数据改变之后，界面的变化会有一定延时。不用timeout有时候会发现界面没有变化
        //setTimeout(done => {
        //    expect(vm.$el.querySelector('.key').textContent).to.equal('hahaha')
        //    done()
        // }, 100)
    })
   
})
