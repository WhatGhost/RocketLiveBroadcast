import Vue from 'vue'
import RoomList from '@/components/RoomList'
// import store from '../../../src/store/store.js'

describe('RoomList.vue Test', () => {
    // 检查原始组件选项
    it('check its default data', () => {
        expect(RoomList.data).to.be.a('function')
        const defaultData = RoomList.data()
        expect(defaultData.num).to.equal(0)
    })
    it('correctly sets the num when created', () => {
        const vm = new Vue(RoomList).$mount()
        expect(vm.num).to.equal(0)
    })
    it('check its import components', () => {
        expect(RoomList.components).to.have.property('Room')
    })
    it('check its computed', () => {
        expect(RoomList.computed).to.have.property('rooms')
        expect(RoomList.computed).to.have.property('count')
    })
    it('check its methods', () => {
        expect(RoomList.methods).to.be.empty
    })
    // 检查mount中的组件实例
    // it('correctly sets the message when created', () => {
    //     const vm = new Vue(RoomList).$mount()
    //     expect(vm.num).to.equal(2)
    // })
    //   // 检查mount中的组件实例
    //   it('correctly sets the message when created', () => {
    //     const vm = new Vue(MyComponent).$mount()
    //     expect(vm.message).toBe('bye!')
    //   })
    //   // 创建一个实例并检查渲染输出
    //   it('renders the correct message', () => {
    //     const Ctor = Vue.extend(MyComponent)
    //     const vm = new Ctor().$mount()
    //     expect(vm.$el.textContent).toBe('bye!')
    //   })
})
