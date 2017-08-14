import {
    destroyVM,
    createTest
} from '../../util'
import Vue from 'vue'
import RegisterModalDialog from '@/components/RegisterModalDialog'

describe('RegisterModalDialog.vue', () => {
    let vm

    afterEach(() => {
        destroyVM(vm)
    })

    it('test default account value', () => {
        vm = new Vue(RegisterModalDialog, true)
        expect(vm.account).to.equal('')
    })
})
