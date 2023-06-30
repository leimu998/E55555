import java.util.Random;
public class xier {
    public static void main(String[] args) {
        float crit_rate_1 = 0.64F;//初始暴击
        float crit_dmg = 3.0F;//初始爆伤（100%+面板200%）
        float dmg_enhancement = 1.488F;//初始增伤(38.8+10)
        float e = 22F;//e单份倍率（220倍率，2-1-1-6分为10份）
        float q = 425F;//q倍率
        float tl_enhance = 0.8F;//天赋增伤
        float res_enhance = 1.2F;//天赋抗性穿透增幅(取1.25或1.2)
        float dmg = 0F;//总伤害
        float avg = 0F;//平均值
        Random random = new Random();
        int cd_count = 0;//如泥cd计时器
        int buff_sust = -1;//buff持续时间计时器

        //流程：eqee eeqe eeeq eee

        for(int i = 0; i < 10000; i++){
            crit_rate_1 = 0.64F;
            cd_count = 0;
            buff_sust = -1;
            //第一次E
            float crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }


            //Q
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1){
                dmg += q * (dmg_enhancement + tl_enhance + 0.15) * res_enhance;
            }else{
                dmg += q * (dmg_enhancement + tl_enhance + 0.15) * crit_dmg * res_enhance;
            }

            //第二次E（含增幅）
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * (dmg_enhancement + tl_enhance) * res_enhance;
                }else{
                    dmg += e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第三次E（含增幅）
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * (dmg_enhancement + tl_enhance) * res_enhance;
                }else{
                    dmg += e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第二轮 第一次E
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第二轮 第二次E
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            

            //第二轮 Q
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1){
                dmg += q * (dmg_enhancement + tl_enhance + 0.15) * res_enhance;
            }else{
                dmg += q * (dmg_enhancement + tl_enhance + 0.15) * crit_dmg * res_enhance;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第二轮 第三次E（含增幅）
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * (dmg_enhancement + tl_enhance) * res_enhance;
                }else{
                    dmg += e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第三轮 第一次E
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第三轮 第二次E
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第三轮 第三次E
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第三轮 Q
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1){
                dmg += q * (dmg_enhancement + tl_enhance + 0.15) * res_enhance;
            }else{
                dmg += q * (dmg_enhancement + tl_enhance + 0.15) * crit_dmg * res_enhance;
            }

            //第四轮 第一次E（含增幅）
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * (dmg_enhancement + tl_enhance) * res_enhance;
                }else{
                    dmg += e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }

            //第四轮 第二次E（含增幅）
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 2 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * (dmg_enhancement + tl_enhance) * res_enhance;
                }else{
                    dmg += e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * res_enhance;
            }else{
                dmg += 6 * e * (dmg_enhancement + tl_enhance) * crit_dmg * res_enhance;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }
            
            //第四轮 第三次E
            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 2 * e * dmg_enhancement;
            }else{
                dmg += 2 * e * dmg_enhancement * crit_dmg;
            }

            for(int j = 0; j < 2; j++){
                crit_determine = (float)random.nextDouble();
                if(crit_determine > crit_rate_1 && cd_count <= 0){
                    crit_rate_1 += 0.36F;
                    buff_sust = 2;
                    cd_count = 3;
                    dmg += e * dmg_enhancement;
                }else{
                    dmg += e * dmg_enhancement * crit_dmg;
                }
            }

            crit_determine = (float)random.nextDouble();
            if(crit_determine > crit_rate_1 && cd_count <= 0){
                crit_rate_1 += 0.36F;
                buff_sust = 2;
                cd_count = 3;
                dmg += 6 * e * dmg_enhancement;
            }else{
                dmg += 6 * e * dmg_enhancement * crit_dmg;
            }
            cd_count--;
            buff_sust--;
            if(buff_sust == 0){
                crit_rate_1 = 0.64F;
            }
            
        }
        avg = dmg/10000;
        System.out.println(avg);

    }
}
