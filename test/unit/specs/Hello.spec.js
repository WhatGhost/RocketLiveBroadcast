import {
    destroyVM,
    createTest
} from '../../util'
import Hello from '@/components/Hello'

describe('Hello.vue', () => {
    let vm

    afterEach(() => {
        destroyVM(vm)
    })

    it('测试获取元素内容', () => {
        vm = createTest(Hello)
        expect(vm.$el.querySelector('.hello h1').textContent).to.equal('Welcome to Your Vue.js App')
        expect(vm.$el.querySelector('.hello h2').textContent).to.have.be.equal('Essential Links')
    })

    it('测试获取Vue对象中数据', () => {
        vm = createTest(Hello)
        expect(vm.msg).to.equal('Welcome to Your Vue.js App')
    })

    it('测试获取DOM中是否存在某个class', () => {
        vm = createTest(Hello, {
            content: 'Hello World'
        }, true)
        expect(vm.$el.classList.contains('hello')).to.be.true
    })
})
