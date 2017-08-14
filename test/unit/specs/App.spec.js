import {
    destroyVM,
    createTest
} from '../../util'
import Vue from 'vue'
import App from '@/App'

describe('App.vue', () => {
    let vm

    afterEach(() => {
        destroyVM(vm)
    })

    it('test currentView', () => {
        vm = createTest(App)
        expect(vm.currentView).to.equal('LiveRoom')
    })
})
